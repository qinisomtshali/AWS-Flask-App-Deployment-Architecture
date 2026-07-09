## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').
## 2025-05-14 - Internal Navigation for Complex Diagrams
**Learning:** Adding a "Jump to detailed description" link within the <figcaption> of a complex architecture diagram significantly improves accessibility for screen reader and keyboard users by providing a direct path to the information parity section.
**Action:** Always include a skip-link in the figcaption of complex diagrams that points to their detailed textual description.
