## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2026-03-28 - Standard HTML Anchors for GFM Compatibility
**Learning:** GitHub Flavored Markdown (GFM) does not support the curly-brace header attribute syntax `{#id}` for internal linking. To ensure reliable internal navigation in documentation, use standard HTML anchors `<a id="anchor-name"></a>` within the headers.
**Action:** Always use `<a id="anchor-name"></a>` for internal anchors in `README.md` to guarantee cross-renderer compatibility.
