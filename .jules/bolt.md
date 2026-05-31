# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2026-05-31 - Iterative Documentation Asset Optimization
**Learning:** Successive rounds of quality reduction (e.g., from Q80 to Q70) on high-resolution diagrams can yield significant further size savings (~18%) with no perceptible visual degradation. Additionally, for LCP assets in READMEs, ensuring synchronous decoding by omitting `decoding="async"` is a valid micro-optimization that prevents paint delays.
**Action:** Re-evaluate previously "optimized" assets for further gains if they remain large; prioritize synchronous decoding for above-the-fold documentation images.
