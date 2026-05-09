# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2025-05-09 - WebP Metadata & Compression
**Learning:** AI-generated WebP assets might not show explicit C2PA/XMP metadata in standard grep searches but can still benefit from high-quality re-encoding (Quality 80, Method 6) to achieve significant (~41%) size reductions without visual degradation.
**Action:** When binary analysis is inconclusive, test re-encoding with Pillow to measure potential gains for documentation LCP.
