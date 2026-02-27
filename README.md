# AWS-Flask-App-Deployment-Architecture

This repository provides an architecture diagram and description for deploying a Flask application on AWS using modern cloud-native services.

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram showing a user accessing a Flask app via an AWS Application Load Balancer, which routes to ECS containers pulling images from ECR."
    width="1024"
    height="1024"
    loading="eager"
    decoding="async"
  />
  <figcaption>Figure 1: High-level architecture for deploying Flask on AWS ECS.</figcaption>
</figure>

## Architecture Overview

The diagram illustrates the flow from the user accessing the app through the **Application Load Balancer (ALB)**, which routes traffic to an **ECS service** running Docker containers. These containers pull the Flask app image from **Amazon ECR**.
