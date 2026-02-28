# AWS-Flask-App-Deployment-Architecture

This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram showing user request flow from Internet through ALB to ECS Flask containers with ECR image registry"
    width="1024"
    height="1024"
    loading="eager"
    decoding="async"
  />
  <figcaption>AWS Flask App Deployment Architecture</figcaption>
</figure>
