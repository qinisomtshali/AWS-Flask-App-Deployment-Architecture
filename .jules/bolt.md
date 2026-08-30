# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. Successive rounds of quality reduction (e.g., Quality 80 to 70) combined with max compression effort (WebP Method 6) can yield double-digit percentage gains (e.g., an additional 18% reduction) even on previously "optimized" architectural diagrams without perceptible visual loss.
**Action:** When optimizing WebP assets, don't stop at Quality 80; test Quality 70 with Method 6 to maximize LCP gains while maintaining legibility.
