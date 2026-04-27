# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2025-05-14 - WebP Re-encoding for LCP
**Learning:** Lossy re-encoding of large diagram assets (e.g., using Pillow at Quality 80) can achieve significant LCP improvements (~41% reduction) in cases where the original file is already stripped of metadata but remains unoptimized for its content type.
**Action:** If binary analysis shows no removable metadata, use lossy re-encoding with high-effort compression (method 6) to find further savings.
