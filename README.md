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

- **User**: Accesses the application via a web browser.
- **Application Load Balancer (ALB)**: Routes incoming traffic to the ECS service.
- **Elastic Container Service (ECS)**: Orchestrates the deployment of Dockerized Flask containers.
- **Elastic Container Registry (ECR)**: Stores and manages the Docker images used by ECS.
