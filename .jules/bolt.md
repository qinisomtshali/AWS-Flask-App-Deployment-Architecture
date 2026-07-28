# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2025-03-28 - Successive Quality Reductions for WebP
**Learning:** WebP images that are already 'optimized' can be further compressed by combining high-effort compression parameters (Pillow WebP Method 6) with Quality 70. This can yield significant double-digit size reductions (~18% in this case) without introducing any perceptible visual degradation or text blurriness.
**Action:** When optimizing architectural diagrams, target Quality 70 with Method 6 to achieve aggressive size reductions while maintaining perfect asset legibility.
