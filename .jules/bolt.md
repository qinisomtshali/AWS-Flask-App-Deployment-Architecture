# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2025-06-06 - Advanced LCP Optimization for Documentation
**Learning:** For primary documentation diagrams (LCP elements), `decoding="async"` can delay the first paint even after download. Combining `decoding="sync"` with `fetchpriority="high"` ensures immediate rendering. Additionally, placing HTML justification comments *inside* complex tags in Markdown can lead to escaped text rendering in some parsers (like Python-Markdown).
**Action:** Use `sync` decoding for hero images. Place performance justification comments outside HTML tags to ensure correct rendering across different Markdown engines.
