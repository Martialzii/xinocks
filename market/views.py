
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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
    }
    return render(request, 'market/subscribe.html', context)


def payment_success(request):
    if request.user.is_authenticated:
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.is_premium = True
        profile.save()
    return render(request, 'market/success.html')


def create_paypal_order(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    plan = SubscriptionPlan.objects.first()
    price = str(plan.price) if plan else "9.99"
    return JsonResponse({
        'verified_price': price,
        'payee_email': settings.PAYPAL_RECEIVER_EMAIL
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