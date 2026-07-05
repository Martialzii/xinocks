from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import SubscriptionPlan, UserProfile


class CreatePaypalOrderTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='tester', password='secret123')
        self.plan = SubscriptionPlan.objects.create(price='12.50')

    def test_authenticated_user_receives_order_payload(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('market:create_paypal_order'))

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['verified_price'], '12.50')
        self.assertEqual(data['currency'], 'USD')
        self.assertIn('order_id', data)
        self.assertEqual(data['payee_email'], 'cyrussifa@yahoo.com')


class PaymentSuccessTests(TestCase):
    def test_pending_user_in_session_is_marked_premium(self):
        user = get_user_model().objects.create_user(username='premium-user', password='secret123')
        session = self.client.session
        session['pending_premium_user_id'] = user.id
        session.save()

        response = self.client.get(reverse('market:payment_success'))

        self.assertEqual(response.status_code, 200)
        profile = UserProfile.objects.get(user=user)
        self.assertTrue(profile.is_premium)
