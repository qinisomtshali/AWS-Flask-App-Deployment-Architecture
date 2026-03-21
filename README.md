# AWS-Flask-App-Deployment-Architecture
This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

<figure>
  <!-- ⚡ Bolt Optimization: Stripped ~140KB of C2PA metadata from architecture-diagram.webp (lossless). -->
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram for deploying a Flask application on AWS showing User, ALB, ECS, and ECR components"
    loading="eager"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>Deployment architecture for a Flask application on AWS using ECS and ECR.</figcaption>
</figure>
