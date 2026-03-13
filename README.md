# AWS-Flask-App-Deployment-Architecture
This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Comprehensive architecture diagram for Flask deployment on AWS: User traffic routes through an ALB to ECS containers that pull images from ECR, all within a secure VPC environment."
    loading="eager"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>Deployment architecture for a Flask application on AWS using ECS and ECR.</figcaption>
</figure>

## Core Components

- **User Access**: Users interact with the Flask application via a web browser or client.
- **Application Load Balancer (ALB)**: Distributes incoming application traffic across multiple targets, such as ECS containers.
- **Amazon ECS (Elastic Container Service)**: A fully managed container orchestration service that runs the Dockerized Flask application.
- **Amazon ECR (Elastic Container Registry)**: Stores and manages Docker container images that are pulled by ECS.
- **VPC & Subnets**: Provides a logically isolated section of the AWS Cloud where resources are launched in a defined virtual network.
- **Security Groups**: Act as a virtual firewall for the instances to control inbound and outbound traffic.
