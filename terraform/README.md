# Terraform Infrastructure

This directory contains Terraform configuration for the DevOps Practical
Challenge.

## Configuration

- `providers.tf`: Terraform and AWS provider requirements.
- `variables.tf`: configurable project name and AWS region.
- `main.tf`: shared configuration and AWS identity data source.
- `outputs.tf`: basic configuration outputs.

## Safety

No AWS infrastructure is created by these starter files.

Before deployment, the project will need an explicit infrastructure design,
security-group rules, resource definitions, cost review, and validation.

## Planned deployment

The intended deployment target is AWS. Terraform will provision the required
resources after the Docker image and CI/CD workflow are ready.
