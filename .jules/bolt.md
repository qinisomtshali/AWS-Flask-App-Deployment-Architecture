## 2025-02-28 - Optimizing documentation-centric repositories
**Learning:** In repositories where documentation is the primary interface, image performance is a critical factor for Core Web Vitals (LCP and CLS). Large, unoptimized images with descriptive names can be significantly reduced in size without losing visual quality by using WebP with appropriate quality settings and renaming to more manageable filenames.
**Action:** Use WebP (quality=80) for diagrams, set explicit width/height to prevent Layout Shift, and use loading='eager' for hero images to optimize LCP.
