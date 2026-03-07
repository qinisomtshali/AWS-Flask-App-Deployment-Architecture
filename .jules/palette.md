## 2025-05-14 - Semantic and Performant Documentation Assets

**Learning:** In documentation-heavy repositories, the documentation itself is the User Interface. Using semantic `<figure>` and `<figcaption>` tags provides superior descriptive context for screen readers compared to standard Markdown image syntax. Additionally, specifying explicit dimensions (`width` and `height`) on these assets prevents Cumulative Layout Shift (CLS), ensuring a stable and pleasant reading experience as images load.

**Action:** Prioritize semantic HTML over basic Markdown for complex diagrams and always include dimensions and modern formats (like WebP) to balance visual clarity with performance and accessibility.
