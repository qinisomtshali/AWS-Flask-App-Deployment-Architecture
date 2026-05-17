## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2025-05-15 - HTML Entity Encoding in Automated Verification
**Learning:** When verifying rendered Markdown documentation using Playwright, special characters like `&` in the source text are often converted to HTML entities (e.g., `&amp;`). Automated checks for text presence must account for this encoding to avoid false negatives.
**Action:** Design verification scripts to check for both the literal text and its common HTML-encoded variants when asserting content presence in rendered documentation.
