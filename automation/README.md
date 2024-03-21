# CI/CD Pipeline for Containerized Java Applications

This repository contains the configuration for a CI/CD pipeline designed to automate the building, testing, and deployment of containerized Java applications.

## Project Structure

```bash
.
├── README.md
└── redis_to_s3_exporter.py
```

## Pipeline Overview

The CI/CD pipeline consists of the following stages:

1. **Build**: Compiles the Java code and builds a Docker image for the application.
2. **Test**: Executes unit tests and integration tests within the Docker container.
3. **Deploy**: Deploys the containerized application to the target environment based on the specified deployment environment (`lambda`, `eks`, or `ecs`).

## Pipeline Configuration

### Stages:

- **build**: Compiles Java code and builds Docker image.
- **test**: Executes tests within the Docker container.
- **deploy**: Deploys the application to the specified environment.

### Variables:

- `IMAGE_NAME`: Name of the Docker image for the Java application.

### Build Stage:

The `build` stage compiles the Java code using Maven and creates a Docker image for the application.

### Test Stage:

The `test` stage runs tests within the Docker container to ensure the reliability and quality of the application.

### Deploy Stage:

The `deploy` stage deploys the containerized application to the target environment based on the value of the `DEPLOY_ENVIRONMENT` variable. Supported environments include AWS Lambda (`lambda`), Amazon EKS (`eks`), and Amazon ECS (`ecs`). Deployment commands are tailored to each environment.

## Usage

1. Configure the pipeline variables and environment settings according to your project requirements.
2. Commit the `.gitlab-ci.yml` file to your repository.
3. Trigger the pipeline by pushing changes to your repository, or manually start the pipeline in your CI/CD platform.
