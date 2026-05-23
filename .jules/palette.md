## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-20 - Documentation Navigation and Direct Anchor Links
**Learning:** For long-form documentation (like architecture READMEs), providing direct anchor links within `<figcaption>` elements to their text-based descriptions significantly improves accessibility for screen reader users and quick-nav users. Additionally, "Back to Top" links at the end of deep technical docs are a simple, high-value UX touch.
**Action:** Always include a "View text-based description" link for complex diagrams and a "Back to Top" link at the footer of extensive documentation files.
