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

- **Application Load Balancer (ALB):** Acts as the entry point for user traffic, distributing requests across the Flask application containers.
- **Amazon ECS (Elastic Container Service):** Orchestrates the deployment and scaling of the Flask app using Docker containers.
- **Amazon ECR (Elastic Container Registry):** Stores the Docker images of the Flask application, which are pulled by ECS during deployment.
- **Docker Containers:** Run the Flask application environment, ensuring consistency across deployments.

## Deployment Workflow

1. **Request Entry:** Users access the Flask application via a URL, which points to the Application Load Balancer (ALB).
2. **Traffic Routing:** The ALB receives the incoming traffic and routes it to an available container within the Amazon ECS service.
3. **Container Orchestration:** Amazon ECS manages the running containers, pulling the latest Flask application image from Amazon ECR as needed.
4. **Application Response:** The Flask application processing the request inside the container sends the response back through the ALB to the user.
