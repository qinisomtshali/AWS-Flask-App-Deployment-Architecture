## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-20 - Internal Navigation for Complex Diagrams
**Learning:** For complex architectural diagrams, adding a "Jump to detailed description" link within the <figcaption> improves UX for all users, particularly those using screen readers or keyboard navigation, by providing a direct path to the textual explanation.
**Action:** Use a descriptive aria-label on skip-links in captions to provide clear context for the navigation target.
