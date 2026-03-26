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

The architecture consists of the following key AWS services:

- **User**: Represents the end-user accessing the application via a web browser or client.
- **Application Load Balancer (ALB)**: Acts as the entry point for incoming traffic, distributing requests to the backend services.
- **Amazon ECS (Elastic Container Service)**: Manages the deployment and scaling of Docker containers running the Flask application.
- **Amazon ECR (Elastic Container Registry)**: A fully managed Docker container registry used to store and manage the Flask application images.
- **Security Groups**: Control inbound and outbound traffic to the ALB and ECS tasks.
- **VPC (Virtual Private Cloud)**: The isolated network environment where the resources are deployed.

## Deployment Workflow

1.  **Image Upload**: The Flask application image is built and pushed to **Amazon ECR**.
2.  **Service Update**: **Amazon ECS** is configured to pull the latest image from ECR.
3.  **Traffic Routing**: A **User** sends a request to the application's URL.
4.  **Load Balancing**: The **Application Load Balancer (ALB)** receives the request and forwards it to an available container in the ECS service.
5.  **Response**: The Flask application processes the request and sends a response back through the ALB to the user.
