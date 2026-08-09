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
   .venv\\Scripts\\python.exe -m pip install -r requirements.txt
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
   .venv\\Scripts\\python.exe manage.py migrate
   ```
5. Run the development server:
   ```bash
   .venv\\Scripts\\python.exe manage.py runserver
   ```

## Foundry Toolkit Agent Inspector

The project now includes a lightweight HTTP agent server for the inspector workflow.

- Start it directly:
  ```bash
  .venv\\Scripts\\python.exe agent_server.py
  ```
- Or use the launcher shim:
  ```bash
  agentdev.cmd run
  ```
- VS Code debug entrypoints are available under [.vscode/launch.json](.vscode/launch.json) and [.vscode/tasks.json](.vscode/tasks.json).

Health check:
```bash
curl http://127.0.0.1:8010/health
```

## Admin Access

Create a superuser with:

```bash
.venv\\Scripts\\python.exe manage.py createsuperuser
```

## Notes

- The PayPal integration is configured for sandbox testing by default.
- Keep `.env` out of version control.

## Martialzii Enterprise Integration

This merge also brings in the enterprise suite assets from the remote repository, including the guardian, storm, and key generation utilities.
