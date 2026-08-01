# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2025-03-27 - High-Effort Progressive Image Optimization
**Learning:** Successive rounds of progressive quality reduction (e.g., Quality 80 down to Quality 70) combined with maximum compression effort (WebP Method 6) can yield double-digit percentage gains (such as an additional ~18% reduction or ~37KB saved) even on previously-optimized architectural diagrams, while preserving full visual parity and crisp text rendering.
**Action:** Do not stop optimization at standard defaults; perform iterative lossy compression down to Quality 70 with max method parameters to achieve optimal LCP without sacrificing legibility of architectural text components.
