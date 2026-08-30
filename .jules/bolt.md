# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2025-05-14 - Cumulative Image Optimization
**Learning:** Successive rounds of optimization can still yield gains. Even if an image was previously optimized, re-evaluating the quality/compression trade-off (e.g., dropping from Quality 80 to 75) combined with proper LCP HTML attributes (`fetchpriority="high"`, `loading="eager"`) ensures the best possible documentation load performance.
**Action:** Don't assume an asset is "done" if it's still a primary LCP candidate. Combine asset compression with browser-hinting attributes for maximum impact.
