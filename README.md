# AWS Flask App Deployment Architecture
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
- **User:** The entry point for application traffic.
- **Application Load Balancer (ALB):** Routes incoming HTTP/HTTPS traffic to the appropriate ECS services.
- **Amazon ECS (Elastic Container Service):** Manages and runs Docker containers for the Flask application.
- **Amazon ECR (Elastic Container Registry):** Stores and manages Docker images used by ECS.
- **Flask Application:** The web application running inside the Docker containers.

## Deployment Workflow
1. **Build & Push:** The Flask application is containerized and the Docker image is pushed to Amazon ECR.
2. **Service Update:** Amazon ECS pulls the latest image from ECR.
3. **Traffic Routing:** The Application Load Balancer receives user requests and distributes them across the running ECS containers.
