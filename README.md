# AWS-Flask-App-Deployment-Architecture

This repository provides an overview of the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through an Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="AWS Flask Deployment Flow: User request -> Application Load Balancer -> ECS Cluster (Docker Containers) -> Amazon ECR (Image Registry)."
    loading="eager"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>Deployment architecture for a Flask application on AWS using ECS and ECR.</figcaption>
</figure>

## Core Components

- **User**: Initiates requests to the application.
- **Application Load Balancer (ALB)**: Distributes incoming traffic across multiple targets, such as ECS containers.
- **Amazon ECS**: A managed container orchestration service that runs the Flask app in Docker containers.
- **Amazon ECR**: A managed container registry where the Flask Docker images are stored.
- **Security Groups**: Virtual firewalls that control inbound and outbound traffic to the ECS tasks.

## Quick Links

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Amazon ECS Documentation](https://docs.aws.amazon.com/ecs/)
- [Amazon ECR Documentation](https://docs.aws.amazon.com/ecr/)
- [AWS ALB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
