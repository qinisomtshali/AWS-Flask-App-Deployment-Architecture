# AWS-Flask-App-Deployment-Architecture

This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.

<!--
  ⚡ Bolt Optimization:
  - Renamed from DALL-E source to architecture-diagram.webp for maintainability.
  - Using <img> instead of Markdown to specify width/height (1024px) to eliminate Cumulative Layout Shift (CLS).
  - loading="eager" and decoding="async" used to optimize Largest Contentful Paint (LCP).
-->
<figure>
  <img
    src="architecture-diagram.webp"
    alt="AWS Flask App Deployment Architecture Diagram"
    loading="eager"
    decoding="async"
    width="1024"
    height="1024"
  >
  <figcaption>AWS Flask App Deployment Architecture</figcaption>
</figure>
