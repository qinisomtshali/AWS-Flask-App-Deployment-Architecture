# AWS Flask App Deployment Architecture

## Overview

This repository documents the architecture for deploying a Flask application on AWS using modern containerization and orchestration services. It provides a visual and descriptive guide to the components involved in a production-ready environment.

## Architecture Diagram

<figure>
  <img
    src="architecture-diagram.webp"
    alt="A comprehensive architecture diagram for deploying a Flask application on AWS, showing the flow from the user's web browser to an Application Load Balancer (ALB), then to an ECS service running Docker containers that pull images from Amazon ECR."
    loading="eager"
    decoding="async"
    width="1024"
    height="1024"
  />
  <figcaption>AWS Flask App Deployment Architecture: User -> ALB -> ECS -> ECR</figcaption>
</figure>

The diagram illustrates the flow from the user accessing the application through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.
