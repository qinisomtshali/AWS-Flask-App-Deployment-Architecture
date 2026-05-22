## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-22 - Stable Cross-Linking in Markdown
**Learning:** Standard Markdown auto-generated anchors (slugs) can be brittle or inconsistent across different renderers (e.g., GitHub vs. local Markdown parsers). Using explicit HTML `<span id="target-id"></span>` inside a heading ensures stable navigation targets that are immune to title changes or parser-specific slugification rules.
**Action:** Use explicit HTML IDs for critical documentation headers when implementing internal "jump links," particularly when linking from nested HTML elements like `<figcaption>` where standard Markdown link syntax is not supported.
