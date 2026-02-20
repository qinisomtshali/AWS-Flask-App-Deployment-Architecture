# AWS Flask App Deployment Architecture

This repository contains an architecture diagram for deploying a Flask application on AWS using modern, scalable services.

## Visual Overview

![Architecture diagram showing a user accessing a Flask application via a web browser. The traffic goes through an AWS Application Load Balancer (ALB) to an ECS service running Docker containers, which are pulled from an Amazon Elastic Container Registry (ECR).](architecture-diagram.webp)

## Deployment Flow

The architecture illustrates the following workflow:

1.  **User Access**: A user accesses the application through a web browser.
2.  **Load Balancing**: The **Amazon Application Load Balancer (ALB)** receives the request and routes traffic to the backend service.
3.  **Container Orchestration**: The Flask application runs as Docker containers within an **Amazon ECS (Elastic Container Service)**.
4.  **Container Registry**: ECS pulls the latest Docker images for the application from **Amazon ECR (Elastic Container Registry)**.
5.  **Traffic Security**: **Security Groups** are used to control inbound and outbound traffic, ensuring the application remains secure.
