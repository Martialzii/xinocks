# Xinocks Marketplace

[![.github/workflows/setup-go.yml](https://github.com/Martialzii/Martialzii-Enterprise/actions/workflows/setup-go.yml/badge.svg)](https://github.com/Martialzii/Martialzii-Enterprise/actions/workflows/setup-go.yml)

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

## Branch Plan Blueprint

A new branch concept is documented in [branch_plan_blueprint.md](branch_plan_blueprint.md) for evolving the current market experience into a modular build idea that supports future plan-source variations.

## GitHub Bounty Roadmap

This project can be used as a practical portfolio piece for open-source bounty work.

### Good starter contributions
- Improve documentation and setup instructions
- Add test coverage for the agent server and marketplace flows
- Improve error handling for the PayPal and agent endpoints
- Add a small CLI or admin helper for local development

### Suggested 30-day plan
1. Finish local setup and document it clearly
2. Add 3–5 quality tests for the current features
3. Open a small pull request focused on one improvement
4. Repeat with another feature or documentation fix to build momentum

### Skills this helps you practice
- Python and Django
- Git and GitHub workflows
- Testing and debugging
- API and server reliability
- CI/CD and documentation hygiene

### Bounty platforms to try
- Algora Bounties: React, Next.js, Python, AI, backend, and documentation projects
- IssueHunt: open-source bug fixes and feature work
- BountyHub: GitHub issues with rewards
- OnlyDust: open-source and Web3 development opportunities

### FastAPI and backend contribution path
Use this repo as a foundation while you build backend experience in parallel.

- Explore FastAPI issues and related repositories to learn contribution patterns
- Build a small FastAPI portfolio project alongside this Django work
- Complete a few beginner-friendly issues before applying for paid bounties
- Use the experience to strengthen your GitHub profile and resume

### Suggested next steps
1. Learn Git and GitHub workflows well
2. Build a small FastAPI portfolio project
3. Complete 5–10 beginner issues
4. Apply for paid bounties on Algora, IssueHunt, or OnlyDust
5. Gradually target larger, higher-paying issues

### Next work grade
Target the next level by turning this repo into a stronger showcase project:
- Add better test coverage for the agent server and marketplace flows
- Improve API reliability and documentation
- Introduce a small backend extension or CLI helper
- Prepare a polished pull request history for future bounty applications
