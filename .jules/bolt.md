# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2025-03-27 - LCP Attributes in Markdown
**Learning:** Standard Markdown image syntax `![]()` does not support the `fetchpriority` attribute, which is critical for LCP optimization. Using HTML `<img>` tags in README.md allows for fine-grained control over `fetchpriority`, `loading`, and `decoding`.
**Action:** Use HTML `<img>` tags for above-the-fold documentation diagrams to ensure they are prioritized by the browser.
