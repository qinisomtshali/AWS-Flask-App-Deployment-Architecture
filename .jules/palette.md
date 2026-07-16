## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-15 - Documentation Skip-Links for Visual Assets
**Learning:** For long or complex architectural diagrams in documentation, providing an internal navigation link (skip-link) within the `<figcaption>` allows screen-reader and keyboard users to jump directly to the text-based description, improving navigation efficiency.
**Action:** Implement `<a href="#target" aria-label="...">Jump to detailed description</a>` inside the `<figcaption>` of large images to assist users in bypassing or accessing descriptive content quickly.
