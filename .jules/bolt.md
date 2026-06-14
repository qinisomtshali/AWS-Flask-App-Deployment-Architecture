# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2025-03-27 - Incremental Asset Optimization
**Learning:** Successive rounds of lossy re-encoding (e.g., reducing WebP Quality from 80 to 70) on complex high-resolution diagrams can yield an additional ~18% file size reduction with no perceptible loss in visual quality or architectural clarity.
**Action:** When optimizing documentation images for LCP, test Quality 70 with Method 6 compression to find the optimal balance between file size and text legibility, as architectural diagrams often tolerate higher compression than photographic content.
