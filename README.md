# AWS-Flask-App-Deployment-Architecture

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram showing a Flask app on AWS. It tracks a user request through an Application Load Balancer (ALB) to a Flask application running on ECS containers, with images pulled from ECR."
    width="1024"
    height="1024"
    loading="eager"
    decoding="async"
  />
  <figcaption>Figure 1: High-level architecture of a Flask application deployment on AWS using ALB, ECS, and ECR.</figcaption>
</figure>

This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.
