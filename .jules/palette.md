## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Resilient Internal Anchors in Markdown
**Learning:** Automatically generated header slugs in Markdown can be unreliable when headers contain emojis (e.g., "🏗️ Core Components") or special characters. Explicit HTML anchors (`<a id="target-id"></a>`) provide a stable target for internal links across different Markdown renderers and platforms.
**Action:** Use explicit HTML anchors for key navigation targets in documentation, especially when headers use emojis or complex formatting.
