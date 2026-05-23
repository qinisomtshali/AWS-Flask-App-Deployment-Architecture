## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description'). Additionally, provide a direct clickable navigation link (e.g., 'See details') within the `<figcaption>` to improve UX for all users.

## 2025-05-16 - GitHub Flavored Markdown (GFM) Anchor Behavior
**Learning:** GFM anchor generation for headers follows specific rules: it lowercases text, replaces spaces with hyphens, and strips non-alphanumeric characters *including emojis*. For example, `## 📦 Core Components` generates the ID `#core-components`, not `#📦-core-components`.
**Action:** When creating internal documentation links to headers containing emojis, exclude the emoji from the href attribute to ensure the link functions correctly.
