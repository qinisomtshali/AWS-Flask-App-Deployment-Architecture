# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2025-05-05 - LCP Attribute Preservation
**Learning:** While 'loading="eager"' is the browser default, explicitly keeping it on LCP elements (like hero diagrams in READMEs) is considered best practice to ensure the browser prioritizes the asset immediately, especially in documentation where the image is the primary content.
**Action:** Avoid removing 'loading="eager"' from above-the-fold images during optimization passes.
