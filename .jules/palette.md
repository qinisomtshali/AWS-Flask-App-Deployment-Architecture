## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) require text-based alternatives or comprehensive lists to ensure accessibility and mitigate potential reading difficulties caused by image artifacts or generated text typos.
**Action:** Always include a 'Core Components' or 'Detailed Description' section immediately following a complex diagram and link them using descriptive captions.

## 2025-05-20 - Markdown Parsing in HTML Blocks
**Learning:** Markdown syntax (like `[text](#link)`) is typically not parsed inside block-level HTML tags such as `<figcaption>`. This leads to broken or unrendered links in the documentation.
**Action:** Use standard HTML `<a>` tags for links within HTML blocks in Markdown files to ensure they are correctly rendered by parsers like GitHub's. Also, ensure anchor IDs follow the parser's normalization rules (e.g., stripping emojis).
