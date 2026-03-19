# AWS-Flask-App-Deployment-Architecture
This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram for deploying a Flask application on AWS. See the 'Core Components' and 'Deployment Workflow' sections for a detailed description."
    loading="eager"
    fetchpriority="high"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>Deployment architecture for a Flask application on AWS using ECS and ECR.</figcaption>
</figure>

## Core Components
- **User:** Accesses the application via a web browser.
- **Application Load Balancer (ALB):** Receives incoming traffic and routes it to the ECS service.
- **Amazon ECS:** Orchestrates the deployment and scaling of Docker containers running the Flask application.
- **Amazon ECR:** Stores the Docker images for the Flask application, which are pulled by ECS during deployment.

## Deployment Workflow
1. The user sends a request to the application.
2. The request is received by the **Application Load Balancer (ALB)**.
3. The ALB routes the traffic to a running container within the **Amazon ECS** service.
4. The ECS service pulls the latest Flask application image from **Amazon ECR** to ensure the containers are up-to-date.
