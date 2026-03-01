## 2025-05-15 - Semantic Diagrams in Documentation

**Learning:** In documentation-heavy repositories, the "UI" is the documentation itself. Using semantic HTML like `<figure>` and `<figcaption>` instead of plain markdown image syntax provides better context for screen readers and a more structured visual layout. Additionally, applying `loading="eager"` and `decoding="async"` to the primary architecture diagram ensures it is treated as a priority (LCP) element while minimizing main-thread impact.

**Action:** Use `<figure>` for technical diagrams in READMEs to pair them with clear, accessible captions. Always include explicit `width` and `height` to prevent layout shifts during documentation loads.
