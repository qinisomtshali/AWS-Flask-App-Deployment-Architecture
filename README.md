# AWS-Flask-App-Deployment-Architecture

<img src="architecture-diagram.webp" alt="Architecture diagram for deploying a Flask application on AWS" width="1024" height="1024" loading="eager" decoding="async">

This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.
