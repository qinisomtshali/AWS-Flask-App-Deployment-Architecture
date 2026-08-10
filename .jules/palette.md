## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-08-10 - Keyboard Navigation skip-link placement
**Learning:** Keyboard/screen-reader users benefit greatly from a skip-link to bypass complex visual elements like architectural diagrams. Placing the standard HTML anchor tag directly before the `<figure>` tag without inline style attributes ensures perfect screen reader layout flow and compatibility with platform sanitization filters.
**Action:** Always implement standard skip-links directly before complex `<figure>` elements referencing downstream headings or content sections.
