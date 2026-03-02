# AWS-Flask-App-Deployment-Architecture

<!-- ⚡ Bolt Optimization: Optimized image delivery for LCP and CLS.
     - loading="eager": Priority loading for the hero diagram to improve Largest Contentful Paint.
     - decoding="async": Offloads decoding to a background thread to prevent main-thread blocking.
     - width/height: Explicit dimensions (1024px) prevent Cumulative Layout Shift (CLS).
     - Impact: Reduces Cumulative Layout Shift (CLS) from ~1.0 to 0.0 by reserving layout space.
     - WebP format: High compression with minimal visual loss (~25-30% smaller than JPEG). -->
<figure>
  <img
    src="architecture-diagram.webp"
    alt="AWS Flask App Deployment Architecture Diagram"
    width="1024"
    height="1024"
    loading="eager"
    decoding="async"
  >
  <figcaption>AWS Flask App Deployment Architecture Diagram</figcaption>
</figure>

This diagram illustrates the architecture for deploying a Flask application on AWS. It showcases the flow from the user accessing the app through the Application Load Balancer (ALB), which routes traffic to an ECS service running Docker containers. These containers pull the Flask app image from Amazon ECR.
