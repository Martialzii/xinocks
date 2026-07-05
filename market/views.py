
import base64
import json
import os
import urllib.request

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Product, SubscriptionPlan, UserProfile


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, 'market/product/list.html', {
        'categories': categories,
        'products': products
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'market/product/detail.html', {'product': product})


@login_required
def subscription_checkout(request):
    plan = SubscriptionPlan.objects.first() or SubscriptionPlan.objects.create()
    context = {
        'plan': plan,
        'paypal_email': settings.PAYPAL_RECEIVER_EMAIL,
        'sandbox_mode': settings.PAYPAL_TEST_MODE,
        'paypal_client_id': settings.PAYPAL_CLIENT_ID or 'sb',
    }
    return render(request, 'market/subscribe.html', context)


def payment_success(request):
    if request.user.is_authenticated:
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.is_premium = True
        profile.save()
    return render(request, 'market/success.html')


@csrf_exempt
def create_paypal_order(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    plan = SubscriptionPlan.objects.first() or SubscriptionPlan.objects.create()
    price = str(plan.price) if plan else '9.99'

    client_id = getattr(settings, 'PAYPAL_CLIENT_ID', None) or os.getenv('PAYPAL_CLIENT_ID', '')
    client_secret = getattr(settings, 'PAYPAL_CLIENT_SECRET', None) or os.getenv('PAYPAL_CLIENT_SECRET', '')
    api_base_url = getattr(settings, 'PAYPAL_API_BASE_URL', 'https://api-m.sandbox.paypal.com').rstrip('/')

    if client_id and client_secret:
        try:
            auth_header = base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()
            token_request = urllib.request.Request(
                f'{api_base_url}/v1/oauth2/token',
                data=b'grant_type=client_credentials',
                method='POST',
                headers={
                    'Authorization': f'Basic {auth_header}',
                    'Accept': 'application/json',
                    'Accept-Language': 'en_US',
                },
            )
            with urllib.request.urlopen(token_request, timeout=20) as token_response:
                token_payload = json.loads(token_response.read().decode())

            access_token = token_payload.get('access_token')
            if not access_token:
                raise RuntimeError('PayPal access token was not returned')

            order_payload = {
                'intent': 'CAPTURE',
                'purchase_units': [{
                    'amount': {
                        'currency_code': 'USD',
                        'value': price,
                    }
                }],
                'application_context': {
                    'return_url': request.build_absolute_uri(reverse('market:payment_success')),
                    'cancel_url': request.build_absolute_uri(reverse('market:subscription_checkout')),
                },
            }
            order_request = urllib.request.Request(
                f'{api_base_url}/v2/checkout/orders',
                data=json.dumps(order_payload).encode(),
                method='POST',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}',
                },
            )
            with urllib.request.urlopen(order_request, timeout=20) as order_response:
                order_data = json.loads(order_response.read().decode())

            return JsonResponse({
                'verified_price': price,
                'currency': 'USD',
                'order_id': order_data.get('id', f'demo-{plan.id}'),
                'payee_email': settings.PAYPAL_RECEIVER_EMAIL,
            })
        except Exception as exc:
            return JsonResponse({
                'verified_price': price,
                'currency': 'USD',
                'order_id': f'demo-{plan.id}',
                'payee_email': settings.PAYPAL_RECEIVER_EMAIL,
                'error': str(exc),
            }, status=502)

    return JsonResponse({
        'verified_price': price,
        'currency': 'USD',
        'order_id': f'demo-{plan.id}',
        'payee_email': settings.PAYPAL_RECEIVER_EMAIL,
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('market:product_list')
    else:
        form = UserCreationForm()
    return render(request, 'market/signup.html', {'form': form})