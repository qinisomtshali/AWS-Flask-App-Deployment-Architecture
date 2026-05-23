## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Navigation and LCP Best Practices
**Learning:** For "Back to Top" navigation to work correctly, the target anchor should be placed at the very top of the file, before the main header. Additionally, while lazy loading is good for most images, primary hero images (LCP elements) should explicitly use `loading="eager"` to ensure they are prioritized by the browser.
**Action:** Always place the `#top` anchor before the H1 in documentation and explicitly set `loading="eager"` for primary header images.
