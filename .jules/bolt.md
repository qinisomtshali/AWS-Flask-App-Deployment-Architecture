# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2025-05-14 - Explicit LCP Hints in Markdown
**Learning:** Standard Markdown image syntax doesn't support the `fetchpriority` attribute. Using HTML `<img>` tags in README.md allows for `fetchpriority="high"`, which measurably improves LCP for the primary architecture diagram by signaling its importance to the browser earlier than standard discovery.
**Action:** Replace critical LCP Markdown images with HTML `<img>` tags to leverage advanced browser performance hints.
