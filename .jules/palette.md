## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Markdown in HTML Figcaption
**Learning:** Markdown link syntax (e.g., `[Text](#link)`) is not parsed when placed inside HTML tags like `<figcaption>`. This results in broken/unrendered links in many Markdown viewers. Additionally, adding excessive navigation elements (like "Back to Top" links) in very short documents can introduce visual noise without significant UX benefit.
**Action:** Use standard HTML `<a>` tags for internal links within `<figcaption>` or other HTML blocks in Markdown files. Evaluate document length before adding navigation helpers to ensure they add genuine value.
