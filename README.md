# AWS Flask App Deployment Architecture

This repository documents the architecture for deploying a Flask application on AWS using modern containerized services.

## Architecture Overview

![Architecture diagram showing a Flask application deployment on AWS. It illustrates a user accessing the app via a web browser, traffic flowing through an Application Load Balancer (ALB) to an ECS service running Docker containers, which are pulled from Amazon ECR.](architecture-diagram.webp)

The diagram illustrates the following flow:
1. **User Access:** A user accesses the application via a web browser.
2. **Application Load Balancer (ALB):** Routes incoming traffic to the ECS service.
3. **Amazon ECS:** Manages the Docker containers running the Flask application.
4. **Amazon ECR:** Serves as the registry for the Flask application Docker images.

## Key Services

- **Application Load Balancer (ALB)**
- **Amazon Elastic Container Service (ECS)**
- **Amazon Elastic Container Registry (ECR)**
- **Security Groups**
