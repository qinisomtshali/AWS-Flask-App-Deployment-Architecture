## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2026-05-31 - Diagram-to-Text Navigation
**Learning:** For long documentation pages with complex architectural diagrams, users benefit from an immediate, contextual link within the diagram's caption that jumps to the relevant textual descriptions. This bridge improves the experience for both visual and non-visual users by reducing the effort to find detailed component explanations.
**Action:** Always include a "Jump to detailed descriptions" link within the `<figcaption>` of a primary architectural diagram that targets the corresponding explanatory text section.
