## 2024-11-20 - Optimizing Documentation Assets
**Learning:** In documentation-heavy repositories, the "UI" is the documentation itself. Large diagrams can cause significant Cumulative Layout Shift (CLS) if dimensions aren't explicitly defined. Setting `loading="eager"` and `decoding="async"` for hero images improves Largest Contentful Paint (LCP) and perceived performance.
**Action:** Always include `width`, `height`, `loading`, and `decoding` attributes for critical documentation images to ensure a stable and fast reading experience.
