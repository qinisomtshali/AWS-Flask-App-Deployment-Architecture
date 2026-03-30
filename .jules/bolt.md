# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2026-03-30 - Markdown Asset Optimization
**Learning:** While GitHub-flavored Markdown strips non-standard attributes like `fetchpriority` and `decoding` for security/sanitization, they remain critical signals for browsers when documentation is viewed via other platforms or as standalone assets. Combining these with explicit `width` and `height` eliminates CLS (Cumulative Layout Shift) even if the more advanced attributes are stripped.
**Action:** Always include explicit dimensions with performance-focused HTML tags in README files to provide a baseline for CLS prevention.
