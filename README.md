# AWS-Flask-App-Deployment-Architecture
This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram for deploying a Flask application on AWS showing User, ALB, ECS, and ECR components"
    loading="eager"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>Deployment architecture for a Flask application on AWS using ECS and ECR.</figcaption>
</figure>

## Core Components
- **User**: Initiates requests to the Flask application.
- **Application Load Balancer (ALB)**: Receives incoming traffic and routes it to the appropriate ECS service.
- **Amazon ECS (Elastic Container Service)**: Manages and runs Docker containers for the Flask application.
- **Amazon ECR (Elastic Container Registry)**: Stores the Docker images used by ECS.
- **Security Groups**: Control inbound and outbound traffic to ensure secure communication between components.
