# Palette's Journal - Critical UX/Accessibility Learnings

## 2025-05-14 - Semantic Documentation for Technical Diagrams
**Learning:** In technical documentation, diagrams are primary content. Using `<figure>` and `<figcaption>` instead of standalone `<img>` tags provides better document structure for screen readers and ensures the explanation (caption) is programmatically linked to the visual.
**Action:** Always wrap architectural diagrams in `<figure>` and use `<figcaption>` for descriptive titles or keys to improve accessibility.
