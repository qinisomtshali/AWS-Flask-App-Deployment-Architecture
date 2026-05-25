<a id="top"></a>

# 🏗️ AWS-Flask-App-Deployment-Architecture
This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the [Application Load Balancer (ALB)](#core-components), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR. Review the [Core Components](#core-components) and [Deployment Workflow](#deployment-workflow) sections below for more details.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram for deploying a Flask application on AWS. See the Core Components section for a detailed description."
    fetchpriority="high"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>Deployment architecture for a Flask application on AWS using ECS and ECR. See the <a href="#core-components">Core Components</a> section for details.</figcaption>
</figure>

<a id="core-components"></a>

## 📦 Core Components

- **Application Load Balancer (ALB):** Acts as the entry point for user traffic, distributing incoming requests across the ECS service.
- **Amazon ECS (Elastic Container Service):** Orchestrates the deployment of Docker containers running the Flask application.
- **Amazon ECR (Elastic Container Registry):** Stores the Docker images for the Flask application, which are pulled by ECS during deployment.
- **Security Groups:** Act as virtual firewalls to control inbound and outbound traffic for the load balancer and ECS tasks.
- **Amazon VPC & Subnets:** Provides the isolated network environment where the application and its resources reside.

<a id="deployment-workflow"></a>

## 🚀 Deployment Workflow

1.  **Image Storage:** The Flask application's Docker image is pushed to Amazon ECR.
2.  **Service Update:** Amazon ECS is configured to pull the latest image from ECR.
3.  **Container Launch:** ECS launches tasks in the service using the specified image.
4.  **Traffic Routing:** The Application Load Balancer (ALB) routes incoming user traffic to the healthy containers in the ECS service.

---

[⬆ Back to top](#top)
