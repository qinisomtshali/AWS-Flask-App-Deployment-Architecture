# AWS-Flask-App-Deployment-Architecture
This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram for deploying a Flask application on AWS. See the Core Components and Deployment Workflow sections for a detailed description."
    loading="eager"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>Deployment architecture for a Flask application on AWS using ECS and ECR.</figcaption>
</figure>

## Core Components

- **User**: Represents the end-user accessing the application via a web browser.
- **Application Load Balancer (ALB)**: Receives incoming traffic and routes it to the ECS service.
- **Amazon ECS (Elastic Container Service)**: Manages and runs the Docker containers for the Flask application.
- **Amazon ECR (Elastic Container Registry)**: Stores the Docker images for the Flask application.

## Deployment Workflow

1. The **User** sends a request to the application.
2. The **Application Load Balancer (ALB)** receives the request and forwards it to an available container in the **Amazon ECS** service.
3. **Amazon ECS** pulls the latest Flask application image from **Amazon ECR** to run the containers.
4. The application processes the request and sends the response back through the ALB to the user.
