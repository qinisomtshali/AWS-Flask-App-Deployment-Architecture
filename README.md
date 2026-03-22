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

- **User**: Represents the end-user accessing the Flask application.
- **Application Load Balancer (ALB)**: Receives incoming HTTP/HTTPS traffic from users and distributes it across multiple targets in an ECS service.
- **Amazon ECS (Elastic Container Service)**: A fully managed container orchestration service that runs the Flask application in Docker containers.
- **Amazon ECR (Elastic Container Registry)**: A managed Docker container registry that stores the Flask application's Docker images.
- **Security Groups**: Act as a virtual firewall for the ECS service to control inbound and outbound traffic.

## Deployment Workflow

1.  The user initiates a request to the Flask application.
2.  The Application Load Balancer (ALB) receives the request and routes it to an available container within the Amazon ECS service.
3.  The ECS service ensures that the required number of Docker containers are running.
4.  Each container pulls the latest Flask application image from Amazon ECR during deployment or scaling events.
5.  Security Groups are configured to ensure that only legitimate traffic reaches the ALB and the ECS service.
