# AWS-Flask-App-Deployment-Architecture
This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

## Core Components
- **User**: The end-user accessing the application through their web browser.
- **ALB (Application Load Balancer)**: Acts as the entry point, routing incoming user traffic to the backend services.
- **ECS (Elastic Container Service)**: Orchestrates the running of Docker containers that host the Flask application.
- **ECR (Elastic Container Registry)**: A secure repository that stores the Docker images used by the ECS service.

## Deployment Workflow
1. The **User** initiates a request to access the Flask application.
2. The **ALB** receives the request and routes it to the available **ECS** service.
3. **ECS** manages the deployment of the application across multiple Docker containers.
4. During scaling or updates, **ECS** pulls the latest container image from **ECR**.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram for deploying a Flask application on AWS. See the Core Components and Deployment Workflow sections for a detailed text-based description."
    loading="eager"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>Deployment architecture for a Flask application on AWS using ECS and ECR.</figcaption>
</figure>
