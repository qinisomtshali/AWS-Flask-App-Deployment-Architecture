## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-15 - Figcaption Skip Links
**Learning:** For complex documentation diagrams, adding a "Jump to detailed description" link directly inside the `<figcaption>` is a high-impact micro-UX win. It provides immediate accessibility for screen-reader and keyboard users to find the textual equivalent of a complex visual.
**Action:** Use the pattern `<figcaption>Description. <a href="#target" aria-label="...">Jump to description</a></figcaption>` for all informative diagrams.
