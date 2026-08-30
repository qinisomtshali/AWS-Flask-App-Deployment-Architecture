# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2025-03-26 - Iterative Image Optimization
**Learning:** Successive rounds of lossy re-encoding (e.g., reducing WebP Quality from 80 to 70) on complex high-resolution diagrams can yield an additional ~18% file size reduction with no perceptible loss in visual quality or architectural clarity, especially when using maximum compression effort (Method 6).
**Action:** When a high-impact asset remains large after initial optimization, test further quality reductions in small increments (e.g., 5%) while maintaining high compression effort to find the optimal size-to-quality ratio.
