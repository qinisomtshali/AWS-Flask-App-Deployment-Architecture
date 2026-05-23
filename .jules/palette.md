## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Integrated Documentation Navigation
**Learning:** Documentation with complex visual assets benefits from bridging the gap between images and text alternatives with direct navigation links. Using `<figcaption>` elements to link to specific text-based sections (e.g., '#core-components') provides a clear visual and semantic affordance for users seeking more detail.
**Action:** Implement direct anchor links within `<figcaption>` and 'Back to Top' navigation for long technical documentation to improve flow and micro-UX.
