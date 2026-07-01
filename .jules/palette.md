## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Internal Navigation for Complex Diagrams
**Learning:** Adding a "Jump to detailed description" skip-link directly in the diagram's `<figcaption>` significantly improves UX for keyboard and screen-reader users by providing an immediate path to information parity, especially when the text description is further down the page.
**Action:** Use a descriptive `aria-label` on skip-links within `<figcaption>` (e.g., `<figcaption><a href="#target" aria-label="Jump to detailed description of the architecture components">[Jump to detailed description]</a></figcaption>`) to assist navigation.
