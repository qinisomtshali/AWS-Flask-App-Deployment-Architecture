# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, successive rounds of lossy re-encoding (Quality 80 -> 75 -> 70) can provide significant LCP boosts (up to ~52% total reduction from original) with negligible visual impact on architectural diagrams.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding (starting at Quality 70) to optimize for LCP without sacrificing legibility of diagram text.
