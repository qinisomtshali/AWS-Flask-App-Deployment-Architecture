## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Internal Navigation for Complex Imagery
**Learning:** For users navigating documentation via keyboard or screen readers, jumping from a complex figure to its textual breakdown can be cumbersome if they have to scroll manually. A "Jump to detailed description" internal link within the `<figcaption>` provides a clear, accessible shortcut that improves navigation flow.
**Action:** Use a descriptive `aria-label` or `title` on internal jump links within figures to ensure their purpose is clear to assistive technologies.
