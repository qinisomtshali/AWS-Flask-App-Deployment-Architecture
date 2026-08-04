## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Internal Document Navigation & Parser Compatibility
**Learning:** When embedding internal documentation links within HTML tags (such as `<figcaption>`) in Markdown files, standard Markdown `[text](#link)` syntax is not correctly rendered by standard Python-based Markdown parsers. Using standard HTML `<a>` tags with explicit `aria-label`s ensures both cross-parser rendering compatibility and screen-reader accessibility for navigation targets.
**Action:** Always use semantic HTML `<a>` tags for links embedded inside outer HTML blocks in Markdown, and provide clear descriptive ARIA labels for non-contextual link text like "(Jump to detailed description)".
