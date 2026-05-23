## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-16 - Document Navigation Patterns
**Learning:** For long documentation, "Back to Top" navigation and direct anchor links within `<figcaption>` elements (linking to text-based descriptions) significantly improve the accessibility and UX by providing immediate wayfinding. Emojis in headers (like 📦 or 🚀) can break standard GitHub auto-generated IDs, so explicit anchors or plain text links are safer for internal navigation.
**Action:** Implement a top anchor `<a id="top"></a>` and footer navigation links in long docs. Use explicit anchor links in figure captions to guide users to detailed text alternatives.
