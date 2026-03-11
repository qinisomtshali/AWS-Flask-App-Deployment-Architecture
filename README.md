# AWS Flask App Deployment Architecture

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=flat&logo=amazon-aws&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)

This repository contains the architecture diagram for deploying a Flask application on AWS.

### 🚀 Request Flow

1.  **User Access**: The user accesses the application.
2.  **Load Balancing**: The **Application Load Balancer (ALB)** receives the traffic.
3.  **Routing**: The ALB routes traffic to an **ECS Service**.
4.  **Containers**: The service runs **Docker containers** pulling the Flask app image from **Amazon ECR**.

### 🛠️ Core Components

*   [**Application Load Balancer (ALB)**](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html): Routes incoming HTTP/HTTPS traffic to targets.
*   [**Amazon Elastic Container Service (ECS)**](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html): A highly scalable, high-performance container orchestration service.
*   [**Amazon Elastic Container Registry (ECR)**](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html): A fully managed Docker container registry.

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
