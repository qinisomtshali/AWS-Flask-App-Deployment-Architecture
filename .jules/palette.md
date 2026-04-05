## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Documentation Navigation and Visual Hierarchy
**Learning:** In documentation-only repositories, the README is the primary interface. Adding "Back to Top" navigation and direct anchor links within `<figcaption>` elements (e.g., linking to text-based descriptions like '#core-components') significantly improves accessibility and document scannability for long technical pages.
**Action:** Implement structural separators (horizontal rules) and contextual navigation links (Back to Top, direct anchors from diagrams to text) to improve the micro-UX of technical documentation.
