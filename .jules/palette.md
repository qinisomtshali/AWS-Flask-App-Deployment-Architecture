## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-15 - Explicit Anchors for Emoji Headers
**Learning:** Markdown renderers (like GitHub) auto-generate header IDs, but headers containing emojis (e.g., `## 📦 Core Components`) often result in inconsistent or messy slugs (e.g., `#-core-components` or encoded strings).
**Action:** Use explicit HTML anchors (e.g., `<a id="core-components"></a>`) before or inside headers with emojis to ensure reliable, clean internal links across all platforms.
