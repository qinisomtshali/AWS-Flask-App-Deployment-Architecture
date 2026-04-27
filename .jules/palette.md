## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-15 - Explicit HTML Anchors for Robust Navigation
**Learning:** Inserting explicit HTML anchors (e.g., `<a id="core-components"></a>`) inside or before headers ensures internal Markdown links function reliably across different platforms and renderers, specifically when headers contain emojis which complicate automatic slugification.
**Action:** Use manual HTML anchors for critical internal navigation targets in documentation to ensure "Skip to text" links and deep links always work as intended.
