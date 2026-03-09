## 2025-03-14 - [Semantic Documentation Assets]

**Learning:** In documentation-heavy repositories, the documentation itself is the "User Interface." Using non-semantic, auto-generated filenames for critical assets like architecture diagrams creates a poor developer experience (DX) and makes the repo harder to navigate. Semantic HTML `<figure>` and `<figcaption>` tags, combined with descriptive `alt` text and explicit image dimensions, significantly improve both accessibility and visual stability (preventing Layout Shift).

**Action:** Always rename auto-generated media filenames to descriptive, kebab-case names. Use semantic HTML for embedding images in READMEs to provide better context for screen readers and improve performance.
