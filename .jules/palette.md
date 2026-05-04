## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Interactive Diagram Captions
**Learning:** While `alt` text provides screen reader accessibility, it doesn't offer a direct way for sighted users to navigate to detailed text alternatives for complex diagrams. Using standard HTML `<a>` tags within a `<figcaption>` element creates an interactive bridge between a visual artifact and its descriptive source.
**Action:** Enhance diagram `<figcaption>` elements with explicit internal links to the corresponding text-based descriptions. Use HTML anchors (`<a id="...">`) for target sections to ensure cross-platform link stability.
