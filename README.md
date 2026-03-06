# AWS-Flask-App-Deployment-Architecture

This repository provides an overview of a scalable architecture for deploying a Flask application on Amazon Web Services (AWS) using containerization and managed services.

## Architecture Overview

The following diagram illustrates the high-level deployment flow:

<figure>
  <img src="architecture-diagram.webp" alt="AWS Flask Deployment Architecture Diagram: User access via ALB, traffic routed to ECS service with Docker containers, pulling images from ECR." width="1024" height="1024" loading="eager" decoding="async">
  <figcaption>Figure 1: High-level AWS Flask Deployment Architecture</figcaption>
</figure>

## Key Technologies

A combination of modern tools and AWS services is used to ensure a scalable and maintainable deployment:

- **Flask**: A lightweight Python web framework for building the application.
- **Docker**: Containerization to ensure consistency across development, testing, and production.
- **Amazon ECS (Elastic Container Service)**: A fully managed container orchestration service to run the Flask application.
- **Amazon ECR (Elastic Container Registry)**: A managed Docker container registry to store and manage container images.
- **Amazon ALB (Application Load Balancer)**: Efficiently routes incoming HTTP/HTTPS traffic to the containers.

## Component Details

- **User Access**: Users interact with the application through a standard web browser.
- **Traffic Routing**: The ALB handles incoming requests, performing health checks and routing traffic to healthy ECS tasks.
- **Scalability**: ECS automatically manages the number of running containers based on demand, ensuring high availability.
- **Image Management**: ECR provides a secure and reliable way to store and version application images.
