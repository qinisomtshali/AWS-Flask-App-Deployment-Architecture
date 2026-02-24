# AWS-Flask-App-Deployment-Architecture

This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

<img src="architecture-diagram.webp" alt="AWS Flask App Deployment Architecture Diagram showing ALB, ECS, and ECR flow" width="1024" height="1024" loading="lazy" decoding="async">

<!-- Performance Optimizations:
- Renamed image to web-friendly filename.
- Used loading="lazy" to defer off-screen image loading.
- Used decoding="async" to reduce main-thread blocking.
- Explicit width/height to prevent Cumulative Layout Shift (CLS).
-->
