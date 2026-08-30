# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2025-06-22 - Optimizing Architecture Diagram WebP
**Learning:** For documentation-only repos, asset optimization is the primary performance win. Re-encoding 'architecture-diagram.webp' using Pillow with quality=70 and method=6 resulted in a consistent 18% size reduction (from 203KB to 166KB) with no perceptual loss in text legibility.
**Action:** Use high-effort lossy re-encoding (Method 6) for WebP assets to maximize LCP benefits when C2PA/metadata stripping is insufficient or not present.
