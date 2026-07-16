# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2024-07-16 - Squeezing Additional Gains from WebP
**Learning:** Successive rounds of quality reduction (e.g., from 80 to 70) combined with maximum compression effort (WebP Method 6) can yield double-digit percentage gains even on previously "optimized" architectural diagrams without perceptible visual loss.
**Action:** When a file is still relatively large, try incremental quality steps (e.g., 70) with `method=6` in Pillow to find the optimal size-to-quality balance.
