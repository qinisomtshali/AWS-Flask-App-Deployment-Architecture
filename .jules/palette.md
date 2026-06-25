## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Jump Links for Diagram Accessibility
**Learning:** Adding a "Jump to detailed description" internal navigation link inside the `<figcaption>` of a complex architectural diagram is an effective UX pattern. It provides an immediate, accessible way for keyboard and screen-reader users to skip to the technical breakdown without searching through the document.
**Action:** Use a descriptive `aria-label` for these skip-links and ensure the target section is a valid ID that receives focus or is scrolled into view.
