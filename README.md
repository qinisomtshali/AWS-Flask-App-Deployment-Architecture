# AWS-Flask-App-Deployment-Architecture
This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. For more details, see the [Core Components](#core-components) and [Deployment Workflow](#deployment-workflow) sections.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram for deploying a Flask application on AWS. See the Core Components section for a detailed description."
    loading="eager"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>Deployment architecture for a Flask application on AWS using ECS and ECR. Detailed descriptions available in <a href="#core-components">Core Components</a> and <a href="#deployment-workflow">Deployment Workflow</a>.</figcaption>
</figure>

## <span id="core-components"></span>📦 Core Components

- **Amazon VPC (Virtual Private Cloud):** The isolated network environment where all resources are deployed.
- **Subnets:** Public and private subdivisions of the VPC that host the ALB and ECS tasks.
- **Security Groups:** Act as virtual firewalls to control inbound and outbound traffic for the ALB and ECS tasks.
- **Application Load Balancer (ALB):** Acts as the entry point for user traffic, distributing incoming requests across the ECS service.
- **Amazon ECS (Elastic Container Service):** Orchestrates the deployment of Docker containers running the Flask application.
- **Amazon ECR (Elastic Container Registry):** Stores the Docker images for the Flask application, which are pulled by ECS during deployment.

## <span id="deployment-workflow"></span>🚀 Deployment Workflow

1.  **Image Storage:** The Flask application's Docker image is pushed to Amazon ECR.
2.  **Service Update:** Amazon ECS is configured to pull the latest image from ECR.
3.  **Container Launch:** ECS launches tasks in the service using the specified image.
4.  **Traffic Routing:** The Application Load Balancer (ALB) routes incoming user traffic to the healthy containers in the ECS service.
