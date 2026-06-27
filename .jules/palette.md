## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2026-06-27 - Figcaption Skip Links
**Learning:** For complex documentation diagrams, a 'Jump to detailed description' internal navigation link inside the <figcaption> is a preferred reusable UX pattern in this repository to assist screen-reader and keyboard users in navigating text alternatives.
**Action:** Implement HTML <a> tags with descriptive aria-labels inside <figcaption> to provide accessible navigation to detailed content sections.
