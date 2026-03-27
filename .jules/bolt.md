# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2025-03-27 - LCP Optimization via fetchpriority
**Learning:** For documentation-heavy sites, the hero image is the primary LCP element. Even if the image is optimally compressed, browsers may still delay its fetch. Adding `fetchpriority="high"` and `loading="eager"` provides a critical hint to the browser's preload scanner to prioritize this asset over others.
**Action:** Use `fetchpriority="high"` on the main hero/LCP element in README or landing pages to achieve faster visual completion.
