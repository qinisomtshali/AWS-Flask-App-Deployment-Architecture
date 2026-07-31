# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2026-07-31 - Extreme Image Compression via Successive Reductions
**Learning:** Successive rounds of quality reduction (e.g., from Quality 80 to 70) combined with max compression effort (WebP Method 6) can yield double-digit percentage size savings (e.g., an additional 18% reduction) even on previously "optimized" architectural diagrams, without causing perceptible visual degradation.
**Action:** When optimizing pre-existing assets, do not stop at Quality 80. Attempt further reduction to Quality 70 with Method 6 and verify visual clarity using `read_image_file`.
