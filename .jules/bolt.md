# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2026-03-06 - WebP Quality 70 Threshold for Architectural Diagrams
**Learning:** Re-encoding architectural WebP diagrams with Pillow using Quality 70 and Method 6 (highest compression effort) achieves an additional 18% size reduction (from 207KB to 170KB) with zero loss in text legibility or diagram clarity.
**Action:** When fine-tuning LCP for static architectural diagrams, Quality 70 with Method 6 provides a safe compression threshold for double-digit gains without visual degradation.
