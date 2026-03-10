## 2025-03-13 - Documentation Asset Optimization
**Learning:** In repositories where documentation (README.md) is the primary user interface, optimizing visual assets for Largest Contentful Paint (LCP) and Cumulative Layout Shift (CLS) is a valid and impactful performance improvement.
**Action:** Always use explicit width/height, loading="eager" for hero images, and decoding="async" for off-main-thread processing in documentation. Renaming long, generated filenames also improves maintainability and path resolution speed.
