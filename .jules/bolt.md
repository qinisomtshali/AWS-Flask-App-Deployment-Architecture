# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2025-03-27 - Lossy WebP Optimization for Documentation
**Learning:** For large AI-generated diagrams, simply stripping metadata (C2PA/XMP) might yield negligible gains if the image was saved with high-effort lossless or very high-quality lossy settings. Re-encoding using Pillow with `quality=80` and `method=6` (highest compression effort) can achieve significant LCP wins (~41%) without visible degradation in typical documentation contexts.
**Action:** If metadata stripping is insufficient, use lossy re-encoding with high compression effort for documentation assets.
