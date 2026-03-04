# AWS-Flask-App-Deployment-Architecture

This repository provides an architecture diagram for deploying a Flask application on AWS using modern cloud-native services.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="AWS Architecture Diagram for Flask Deployment: User -> ALB -> ECS (Fargate) -> ECR"
    width="1024"
    height="1024"
    loading="eager"
    decoding="async"
  />
  <figcaption>AWS Flask Deployment Architecture: Showcasing the flow from a web browser through an Application Load Balancer to Dockerized Flask containers in Amazon ECS.</figcaption>
</figure>

## Architecture Overview

The architecture showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.
