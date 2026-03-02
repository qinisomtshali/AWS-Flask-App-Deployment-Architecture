## 2025-03-14 - Semantic Documentation Images
**Learning:** In technical documentation, the interface is the text and diagrams themselves. Using semantic HTML like `<figure>` and `<figcaption>` instead of bare Markdown images provides better screen reader context and allows for precise performance optimizations (like explicit dimensions to prevent CLS).
**Action:** Always wrap key architectural diagrams in `<figure>` tags with descriptive captions and performance attributes (width/height/loading) to treat documentation as a high-quality UI component.
