## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2026-05-18 - Avoid Inline Styles in Markdown HTML
**Learning:** When adding HTML elements (such as anchor tags) within Markdown files, using inline CSS/style attributes will fail because platform sanitization filters (like GitHub's) strip out inline styles in rendered previews.
**Action:** Keep embedded HTML in Markdown standard and semantic without custom inline styles, utilizing native elements and default styles for reliable rendering across platforms.
