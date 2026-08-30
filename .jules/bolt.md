# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2026-06-11 - Iterative Image Optimization
**Learning:** Successive rounds of lossy re-encoding on complex high-resolution diagrams (reducing WebP Quality from 80 to 70 with Method 6 effort) can yield an additional ~18% file size reduction with no perceptible loss in architectural clarity.
**Action:** When basic optimization reaches a plateau, use Pillow's highest compression effort (method 6) and slightly lower quality targets (70) to push LCP gains further on critical hero images.
