# Bolt's Journal - Critical Learnings

## 2025-03-13 - Optimizing Documentation Image Delivery
**Learning:** Large documentation images with unoptimized filenames and missing metadata can lead to poor LCP and high CLS in the documentation interface (README). Renaming files to be descriptive and using explicit HTML attributes (`width`, `height`, `loading`, `decoding`) significantly improves both the developer experience and the documentation's perceived performance.
**Action:** Always use explicit dimensions and performance-oriented loading strategies for documentation hero images to prevent layout shifts.
