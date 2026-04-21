# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2026-04-21 - LCP Image Optimization
**Learning:** For images that serve as the Largest Contentful Paint (LCP) element, `loading="eager"` is redundant as it is the browser default. The `fetchpriority="high"` attribute is a more effective signal for the browser's preload scanner to prioritize the asset, directly improving LCP.
**Action:** Remove `loading="eager"` from hero images and apply `fetchpriority="high"` instead, while maintaining explicit dimensions and `decoding="async"`.
