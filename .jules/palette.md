## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-15 - Documentation Navigation via Figure Captions
**Learning:** Navigation links within image captions (`<figcaption>`) significantly enhance the micro-UX of technical documentation by providing a fast path from visual representations to their detailed textual explanations. This is especially helpful for large diagrams that may require scrolling to find the relevant description.
**Action:** Use standard HTML `<a>` tags inside `<figcaption>` to create cross-references to detailed description sections, ensuring the `href` matches a stable header slug or explicit anchor ID.
