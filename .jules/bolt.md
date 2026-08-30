# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2025-03-27 - Incremental Image Optimization
**Learning:** Successive rounds of optimization (e.g., moving from Quality 80 to Quality 70) can still yield meaningful performance gains (18% in this case) without sacrificing the legibility of technical architectural diagrams. High-effort compression methods (Pillow Method 6) are essential for maximizing these gains.
**Action:** When initial optimization is insufficient or further gains are possible, test lower quality levels (down to 70) while specifically verifying text sharpness in diagrams.
