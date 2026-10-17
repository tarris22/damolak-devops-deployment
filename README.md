# DevOps Engineer Practical Challenge

## Project Overview

A small Flask web application developed to demonstrate a production-oriented
DevOps workflow, including automated testing, containerization, CI/CD,
Infrastructure as Code, cloud deployment, and monitoring.

## Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Returns application information and status |
| `/health` | Returns the application health status |

## Technology Stack

- Python and Flask
- Pytest
- Docker
- Jenkins CI/CD
- Terraform
- AWS
- Amazon CloudWatch

## Run Locally

Create and activate a virtual environment, then install dependencies.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Start the application:

```powershell
python -m flask --app app.main run --host 127.0.0.1 --port 5000
```

Open `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/health`.

## Run Tests

Install pytest if necessary:

```powershell
python -m pip install pytest
python -m pytest -v
```

## Planned CI/CD Workflow

1. Retrieve source code from GitHub.
2. Install dependencies and run tests.
3. Build a Docker image.
4. Deploy the application to AWS.
5. Monitor application and infrastructure using CloudWatch.

## Infrastructure as Code

Terraform configuration will be added to provision the required AWS resources.

## Deployment Status

Local application and automated tests are working. Docker execution,
Jenkins automation, Terraform provisioning, AWS deployment, and monitoring
will be completed and verified in subsequent stages.
