# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2026-04-06 - LCP Optimization via fetchpriority
**Learning:** For hero images in documentation (like architecture diagrams), using `fetchpriority="high"` on `<img>` tags can measurably improve Largest Contentful Paint (LCP) by signaling to the browser to prioritize the asset. Explicitly removing `loading="eager"` is a good practice as it is the default behavior and redundant.
**Action:** Use standard `<img>` tags with `fetchpriority="high"` for the first fold visual assets in README files.
