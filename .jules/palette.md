## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2026-06-24 - Accessible Internal Navigation for Diagrams
**Learning:** For complex architectural diagrams, adding a "[Jump to detailed description]" link within the <figcaption> provides an efficient way for keyboard and screen-reader users to skip visual information and access technical details directly.
**Action:** Use an HTML <a> tag with a descriptive aria-label inside <figcaption> to provide accessible internal navigation to text-based alternatives.
