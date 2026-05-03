## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Connecting Captions to Text Alternatives
**Learning:** Even when text alternatives exist, they can be hard to find if the documentation is long. Adding explicit HTML anchors to headers and linking to them from the `<figcaption>` creates a seamless transition for users who want to dive deeper into the details mentioned in an image's `alt` text.
**Action:** Use explicit HTML anchors (`<a id="..."></a>`) in headers and provide internal links within `<figcaption>` to directly connect visual assets to their corresponding technical descriptions.
