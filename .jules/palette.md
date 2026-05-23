## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Contextual Documentation Links
**Learning:** In technical documentation, providing direct, visible navigation between visual diagrams and their detailed textual descriptions (e.g., using a link within a `<figcaption>`) significantly reduces cognitive load and improves accessibility compared to relying on `alt` text alone.
**Action:** Use semantic `<figure>` and `<figcaption>` elements for architectural diagrams and include an anchor link (e.g., `<a href="#-core-components">`) in the caption to bridge the gap between visuals and text.
