# AWS-Flask-App-Deployment-Architecture

<figure>
  <img
    src="architecture-diagram.webp"
    alt="Architecture diagram showing a Flask application deployed on AWS using ALB, ECS, and ECR. A user accesses the app via a web browser, traffic is routed through an Application Load Balancer to Docker containers running in an ECS service, which pulls the app image from Amazon ECR."
    width="1024"
    height="1024"
    loading="eager"
    decoding="async"
  />
  <figcaption>AWS Flask App Deployment Architecture: User -> ALB -> ECS (Docker) -> ECR</figcaption>
</figure>

This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.
