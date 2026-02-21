# AWS Flask App Deployment Architecture

This repository documents the architecture for deploying a Flask application on AWS using modern, scalable, and high-performance containerized services.

## Architecture Overview

<img src="architecture-diagram.webp" alt="Architecture diagram showing a user accessing a Flask application via a web browser. The traffic goes through an AWS Application Load Balancer (ALB) to an ECS service running Docker containers, which are pulled from an Amazon Elastic Container Registry (ECR)." width="1024" height="1024" loading="lazy" decoding="async">

*Optimization: The image above is served with `loading="lazy"` to defer loading until it's in the viewport, and `decoding="async"` to prevent blocking the main thread. Dimensions are explicitly set to avoid layout shifts.*

## Deployment Flow

The architecture illustrates the following workflow:

1.  **User Access**: A user accesses the application through a web browser.
2.  **Load Balancing**: The **Amazon Application Load Balancer (ALB)** receives the request and routes traffic to the backend service.
3.  **Container Orchestration**: The Flask application runs as Docker containers within **Amazon ECS (Elastic Container Service)**.
4.  **Container Registry**: ECS pulls the latest Docker images for the application from **Amazon ECR (Elastic Container Registry)**.
5.  **Traffic Security**: **Security Groups** control inbound and outbound traffic, ensuring the application remains secure.

## Performance Optimizations

To ensure this architecture operates at peak performance, the following AWS best practices should be implemented:

- **Amazon CloudFront**: Add a CDN in front of the ALB to cache static content at edge locations, reducing latency for global users.
- **VPC Endpoints**: Use Interface VPC Endpoints for ECR and S3 Gateway Endpoints. This allows ECS nodes to pull container images and access storage via the AWS private network, significantly speeding up pull times and reducing data transfer costs.
- **Horizontal Auto-scaling**: Configure ECS Service Auto Scaling to automatically adjust the number of running tasks based on real-time traffic demand (e.g., CPU or Request Count).
- **Lightweight Images**: Optimize the Flask Docker image using multi-stage builds and minimal base images (like `python:3.11-slim`) to reduce image size and pull latency.
