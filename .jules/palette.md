## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-06-10 - Documentation Navigation for Accessibility
**Learning:** For long documentation pages with complex visual assets, providing a direct "Jump to" link within the asset's caption (e.g., `<figcaption>`) significantly improves the experience for keyboard and screen reader users by allowing them to skip visual detail and access descriptive content immediately.
**Action:** Add internal skip-links within HTML figure captions in Markdown to link visual assets directly to their detailed textual descriptions.
