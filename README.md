# AWS-Flask-App-Deployment-Architecture
This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram showing user traffic flowing through an Application Load Balancer to a Flask app in ECS containers within a VPC, with images pulled from Amazon ECR."
    loading="eager"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>Deployment architecture for a Flask application on AWS using ECS and ECR. See the <a href="#core-components">Core Components</a> and <a href="#deployment-workflow">Deployment Workflow</a> sections for details.</figcaption>
</figure>

## <span id="core-components"></span>📦 Core Components

- **Application Load Balancer (ALB):** Acts as the entry point for user traffic, distributing incoming requests across the ECS service.
- **Amazon ECS (Elastic Container Service):** Orchestrates the deployment of Docker containers running the Flask application.
- **Amazon ECR (Elastic Container Registry):** Stores the Docker images for the Flask application, which are pulled by ECS during deployment.
- **Amazon VPC (Virtual Private Cloud):** Provides an isolated network environment for the application and its resources.
- **Security Groups:** Act as a virtual firewall for the ECS containers, controlling inbound and outbound traffic.

## <span id="deployment-workflow"></span>🚀 Deployment Workflow

1.  **Image Storage:** The Flask application's Docker image is pushed to Amazon ECR.
2.  **Service Update:** Amazon ECS is configured to pull the latest image from ECR.
3.  **Container Launch:** ECS launches tasks in the service using the specified image.
4.  **Traffic Routing:** The Application Load Balancer (ALB) routes incoming user traffic to the healthy containers in the ECS service.
