## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-06-20 - Skip-Links for Complex Diagrams
**Learning:** For complex architectural diagrams in documentation, providing a "Jump to detailed description" link within the `<figcaption>` significantly improves UX for keyboard and screen-reader users by allowing them to skip the visual asset and navigate directly to the text-based breakdown.
**Action:** Use an internal anchor link in `<figcaption>` to point to the relevant descriptive section of the README when including complex diagrams.
