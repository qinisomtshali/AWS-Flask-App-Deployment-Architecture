
## 2026-02-27 - Layout Shift Prevention in Documentation
**Learning:** Large documentation assets without explicit dimensions cause Cumulative Layout Shift (CLS) when the page is rendered, especially in Markdown previews or static site generators.
**Action:** Always use HTML <img> tags instead of standard Markdown ![]() syntax for large assets to specify 'width' and 'height'. Combine with 'loading' and 'decoding' attributes to optimize Largest Contentful Paint (LCP) and main thread availability.
