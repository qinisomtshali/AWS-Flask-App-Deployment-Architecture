## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-20 - Navigation to Image Descriptions
**Learning:** Adding a direct "Jump to" link in the `<figcaption>` of a complex diagram improves the discoverability of its text-based alternative. While `alt` text provides information to screen readers, a visible navigation link assists all users in quickly finding detailed technical context that might be difficult to parse from the image alone.
**Action:** Include a 'Jump to detailed descriptions' link within the `<figcaption>` targeting the relevant documentation section when using complex visual assets.
