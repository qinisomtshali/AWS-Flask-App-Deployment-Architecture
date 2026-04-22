# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2025-03-27 - Performance Theater in Markdown
**Learning:** Modern LCP attributes like `fetchpriority` and `decoding` are often stripped by Markdown renderers (e.g., GitHub's sanitizer) to prevent XSS or non-standard HTML. While they pass local verification in Playwright, their production impact is often zero in documentation files.
**Action:** Prioritize standard attributes like `width` and `height` to prevent CLS, and treat non-standard attributes as "best-effort" enhancements with limited production expectations in sanitized environments.
