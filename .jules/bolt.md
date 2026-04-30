# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2025-04-30 - Lossy Optimization Win
**Learning:** Lossy re-encoding of large WebP diagram assets using Pillow (Quality 80, high-effort method 6 compression) can achieve significant LCP improvements (e.g., ~41% reduction in 'architecture-diagram.webp') when metadata stripping is not an option.
**Action:** Use Python with the Pillow library (pip install Pillow) for lossy re-encoding when simple metadata stripping is insufficient.
