# AWS-Flask-App-Deployment-Architecture
This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

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

## Core Components

The architecture consists of the following key AWS services and components:

- **User**: Represents the end-user accessing the Flask application via a web browser or client.
- **Application Load Balancer (ALB)**: Automatically distributes incoming application traffic across multiple targets, such as ECS tasks, in multiple Availability Zones.
- **Amazon ECS (Elastic Container Service)**: A fully managed container orchestration service that runs the Docker containers for the Flask application.
- **Amazon ECR (Elastic Container Registry)**: A fully managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images.
- **Security Groups**: Acts as a virtual firewall for the ECS tasks and ALB to control inbound and outbound traffic.

## Deployment Workflow

1. **Image Storage**: The Flask application's Docker image is built and pushed to **Amazon ECR**.
2. **Task Execution**: **Amazon ECS** pulls the latest image from ECR to run as tasks within a service.
3. **Traffic Routing**: When a **User** accesses the application, the request first hits the **Application Load Balancer (ALB)**.
4. **Service Access**: The ALB routes the traffic to one of the healthy Flask application containers running in ECS.
5. **Response**: The Flask application processes the request and sends the response back through the ALB to the User.
