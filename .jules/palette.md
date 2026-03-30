## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2026-03-30 - Reliable Internal Navigation Links
**Learning:** GitHub-flavored Markdown strips emojis and special characters from headers when generating IDs. Using emojis in headers like "## 📦 Core Components" results in a slug like "core-components", not "#-core-components". To ensure accessible and reliable internal navigation, headers should ideally be plain text or explicitly verified against the environment's slugification rules.
**Action:** Avoid emojis in technical headers where internal linking is required, or verify generated IDs before implementation.
