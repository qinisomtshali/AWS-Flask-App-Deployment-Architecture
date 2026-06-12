# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 70-80) with high compression effort (Method 6) can provide significant size reductions (~18% even after previous optimizations) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. Use Pillow for high-effort lossy re-encoding (Quality 70, Method 6) to optimize for LCP without sacrificing text legibility in diagrams.
