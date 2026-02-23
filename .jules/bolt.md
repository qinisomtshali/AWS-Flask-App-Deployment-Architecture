# Bolt's Journal - Critical Performance Learnings

## 2025-05-15 - Documentation as UI Performance
**Learning:** In repositories where documentation (README.md) is the primary user interface, performance optimizations like preventing Cumulative Layout Shift (CLS) and enabling asynchronous image decoding are critical for a "fast" user experience.
**Action:** Always use explicit `width` and `height` attributes and `decoding="async"` for images in documentation to ensure smooth rendering and no layout jumps.
