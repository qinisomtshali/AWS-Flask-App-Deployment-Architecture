## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Documentation Navigation & Accessibility
**Learning:** For documentation-only repositories, the README is the UI. Adding internal navigation anchors (like 'Back to Top') and contextual links within image captions significantly improves the scannability and accessibility of technical content, especially when providing text-based alternatives for complex diagrams.
**Action:** Implement a `#top` anchor and 'Back to Top' links in long documentation files. Ensure `<figcaption>` elements contain direct links to the text sections they describe to facilitate quick navigation for all users.
