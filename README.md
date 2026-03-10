# AWS-Flask-App-Deployment-Architecture

<!-- ⚡ Bolt Optimization: Use explicit dimensions, eager loading, and async decoding to improve LCP and prevent CLS -->
<img src="architecture-diagram.webp" alt="AWS Flask App Deployment Architecture" width="1024" height="1024" loading="eager" decoding="async">

This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.
