# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2025-03-26 - Iterative Quality Scaling
**Learning:** Successive rounds of quality reduction (e.g., from Quality 80 down to Quality 70) combined with max compression effort (WebP Method 6) can yield double-digit percentage gains (such as an additional 18.00% size reduction) on architectural diagrams without any perceptible loss in text legibility or visual quality.
**Action:** When optimizing WebP diagrams, test a range of quality factors (70–80) combined with maximum compression effort (Method 6) to find the absolute sweet spot for LCP performance without degrading detailed elements.
