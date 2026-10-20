# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2025-05-18 - High-Effort WebP Re-encoding on Pre-optimized Diagrams
**Learning:** Successive rounds of WebP re-encoding with Pillow using Quality 70 and Method 6 (highest compression effort) on previously optimized architecture diagrams yield significant size reductions (~18% smaller payload) while preserving the high visual legibility of diagram text and connectors.
**Action:** For documentation LCP optimization, test Quality 70 with Method 6 on WebP diagrams to push asset byte reduction further without degrading visual quality.
