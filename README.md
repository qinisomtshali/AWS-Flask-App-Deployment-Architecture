# AWS-Flask-App-Deployment-Architecture
This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram for deploying a Flask application on AWS. See the Core Components section for a detailed description."
    loading="eager"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>Deployment architecture for a Flask application on AWS using ECS and ECR.</figcaption>
</figure>

## Core Components
- **Client (User)**: Accesses the Flask application via a web browser or API client.
- **Application Load Balancer (ALB)**: Receives incoming traffic and distributes it across multiple healthy targets (ECS tasks) in multiple Availability Zones.
- **Amazon ECS (Elastic Container Service)**: A fully managed container orchestration service that runs the Flask application containers.
- **Amazon ECR (Elastic Container Registry)**: A Docker container registry used to store and manage the Flask application's container images.
- **Security Groups**: Acts as a virtual firewall for the ALB and ECS tasks to control inbound and outbound traffic.

## Deployment Workflow
1. **Containerize**: The Flask application is packaged into a Docker image.
2. **Push to ECR**: The Docker image is pushed to an Amazon ECR repository.
3. **Task Definition**: An ECS task definition is created, referencing the image in ECR.
4. **Service Update**: The ECS service is updated to use the new task definition, triggering a rolling deployment.
5. **Traffic Routing**: The ALB detects new tasks and begins routing traffic to them once they pass health checks.
