# RUN.md

## Automated Pull Request Deployment with Docker and GitHub Actions

This guide explains how to run, configure, and test the automated PR deployment system locally and in GitHub.

---

## Overview

This project automatically deploys every Pull Request into an isolated Docker container for preview and testing.

It does the following:

- Creates a new container when a PR is opened
- Updates the same container when new commits are pushed to the PR
- Posts deployment status and preview links back to the PR
- Cleans up containers and related resources when the PR is closed

---

## Architecture

### Main Components

- **Docker**: Builds and runs isolated PR environments
- **GitHub Actions**: Automates deployment and cleanup workflows
- **GitHub Bot / GitHub App**: Comments on PRs with status updates and preview URLs
- **Deployment Server**: Hosts Docker containers for PR previews

---

## Prerequisites

Make sure the following are available before running the system:

- Git
- Docker
- Docker Compose
- Node.js or Python (depending on your bot implementation)
- GitHub repository with Actions enabled
- A Linux server or VPS with Docker installed
- Domain or subdomain for PR previews, for example:
  - `pr-12.preview.example.com`
  - `pr-15.preview.example.com`

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
GITHUB_APP_ID=your_github_app_id
GITHUB_PRIVATE_KEY_PATH=./private-key.pem
GITHUB_WEBHOOK_SECRET=your_webhook_secret
GITHUB_TOKEN=your_github_token

DEPLOY_HOST=your-server-ip
DEPLOY_USER=ubuntu
DEPLOY_BASE_DIR=/opt/pr-deployments

DOMAIN=preview.example.com
DOCKER_NETWORK=pr_preview_network

APP_PORT_START=5000
NGINX_PORT=80