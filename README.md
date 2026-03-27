# AWS-Flask-App-Deployment-Architecture
This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram for deploying a Flask application on AWS. It shows a user accessing a laptop, traffic flowing through an Application Load Balancer (ALB) to ECS-managed containers, and integration with ECR, Security Groups, and VPC subnets."
    loading="eager"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>Deployment architecture for a Flask application on AWS using ECS and ECR. <a href="#-core-components">See text-based description below</a>.</figcaption>
</figure>

## 📦 Core Components

- **Application Load Balancer (ALB):** Acts as the entry point for user traffic, distributing incoming requests across the ECS service.
- **Amazon ECS (Elastic Container Service):** Orchestrates the deployment of Docker containers running the Flask application.
- **Amazon ECR (Elastic Container Registry):** Stores the Docker images for the Flask application, which are pulled by ECS during deployment.
- **Security Groups:** Act as a virtual firewall for your service to control inbound and outbound traffic.
- **VPC & Subnets:** Provide a logically isolated section of the AWS Cloud where you can launch AWS resources in a defined virtual network.

## 🚀 Deployment Workflow

1.  **Image Storage:** The Flask application's Docker image is pushed to Amazon ECR.
2.  **Service Update:** Amazon ECS is configured to pull the latest image from ECR.
3.  **Container Launch:** ECS launches tasks in the service using the specified image.
4.  **Traffic Routing:** The Application Load Balancer (ALB) routes incoming user traffic to the healthy containers in the ECS service.

---

[↑ Back to Top](#aws-flask-app-deployment-architecture)
