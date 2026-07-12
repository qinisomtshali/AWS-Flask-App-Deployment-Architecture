# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2025-03-27 - Cumulative WebP Optimization
**Learning:** Successive rounds of quality reduction (e.g., 80 to 70) combined with max compression effort (Method 6) can yield double-digit percentage gains even on previously "optimized" assets without perceptible visual loss in architectural diagrams.
**Action:** When LCP is the priority, push WebP Method to 6 and iteratively test Quality down to 70 for documentation diagrams.
