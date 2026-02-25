## 2025-03-13 - Preventing Layout Shift and Optimizing LCP in Documentation

**Learning:** Technical documentation is the "UI" of an architecture repository. Missing image dimensions lead to Cumulative Layout Shift (CLS) when the diagram loads. However, applying `loading="lazy"` to a "hero" diagram or the primary visual content can negatively impact Largest Contentful Paint (LCP) and perceived performance.

**Action:** Always include explicit `width` and `height` attributes for diagrams to stabilize the layout. Use `loading="eager"` for primary/above-the-fold diagrams to ensure rapid rendering, and use `decoding="async"` to prevent the main thread from being blocked during image decoding.
