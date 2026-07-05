# Xinocks Marketplace

Xinocks Marketplace is a Django-based storefront with product browsing, user registration, and a PayPal-powered premium subscription flow.

## Features

- Product listing and product detail pages
- User signup and login
- Premium subscription checkout flow
- PayPal order creation via server-side payload
- Admin support for managing products and subscription plans

## Tech Stack

- Python 3.14+
- Django 6.0+
- SQLite (default development database)
- PayPal Sandbox integration

## Local Development

1. Create and activate a virtual environment (optional but recommended)
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with at least:
   ```env
   SECRET_KEY=your-secret-key
   PAYPAL_RECEIVER_EMAIL=your-sandbox-business-email
   PAYPAL_CLIENT_ID=your-sandbox-client-id
   PAYPAL_CLIENT_SECRET=your-sandbox-client-secret
   PAYPAL_TEST_MODE=True
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Admin Access

Create a superuser with:

```bash
python manage.py createsuperuser
```

## Notes

- The PayPal integration is configured for sandbox testing by default.
- Keep `.env` out of version control.
