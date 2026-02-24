# AWS Flask App Deployment Architecture

This project documents a robust architecture for deploying a Flask application on AWS using modern containerization and orchestration practices.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Detailed AWS architecture diagram: User traffic enters via ALB, flows to ECS-managed Flask containers. Images are pulled from ECR, and traffic is secured by Security Groups within a VPC."
    width="1024"
    height="1024"
    loading="lazy"
    decoding="async"
  >
  <figcaption><i>Figure 1: High-level architecture of the Flask application deployment on AWS.</i></figcaption>
</figure>

## Key Components

- **Application Load Balancer (ALB):** Serves as the entry point, distributing incoming traffic to the containerized application.
- **Amazon ECS (Elastic Container Service):** Orchestrates the deployment and scaling of Flask containers.
- **Amazon ECR (Elastic Container Registry):** Stores and manages the Docker images for the application.
- **Security Groups:** Act as a virtual firewall to control inbound and outbound traffic for the ECS services.
- **VPC & Subnets:** Provide an isolated network environment for the AWS resources.

## Architecture Workflow

1. **User Access:** The user initiates a request via a web browser.
2. **Load Balancing:** The **ALB** receives the request and forwards it to a healthy **ECS container**.
3. **App Execution:** The **Flask application** within the container processes the request.
4. **Image Management:** **ECS** pulls the application image from **ECR** during deployment or scaling events.
5. **Security & Networking:** All traffic is governed by **Security Groups** within a secure **VPC** environment.
