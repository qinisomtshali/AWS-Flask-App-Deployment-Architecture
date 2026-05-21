## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-22 - Internal Navigation for Complex Documentation
**Learning:** In documentation-heavy repositories, users often need to jump between high-level visuals (diagrams) and detailed descriptions. Using semantic HTML anchors (`<span id="...">`) inside Markdown allows for precise navigation that works across various Markdown renderers and improves UX for both keyboard and screen reader users.
**Action:** Implement bidirectional links between complex diagrams and their textual descriptions using consistent ID naming and descriptive link text.
