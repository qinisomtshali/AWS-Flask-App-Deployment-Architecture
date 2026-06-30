## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Skip-links for Diagram Navigability
**Learning:** For complex diagrams in documentation, simply having alt text or nearby descriptions isn't always enough for efficient navigation. A dedicated skip-link within the `<figcaption>` provides an immediate, accessible path for keyboard and screen-reader users to jump to the relevant detailed text description.
**Action:** Add a "Jump to detailed description" internal anchor link within the `<figcaption>` of complex images, ensuring it has a descriptive `aria-label` for context.
