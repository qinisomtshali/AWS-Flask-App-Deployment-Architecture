# AWS-Flask-App-Deployment-Architecture

<figure>
  <img
    src="architecture-diagram.webp"
    alt="AWS Architecture Diagram for Flask Deployment"
    width="1024"
    height="1024"
    loading="eager"
    decoding="async"
  />
  <figcaption>Architecture for deploying a Flask application on AWS using ALB, ECS, and ECR.</figcaption>
</figure>

This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.
