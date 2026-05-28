# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2025-05-28 - Tag-Specific Verification in Documentation
**Learning:** When verifying the removal of HTML attributes (e.g., `decoding="async"`) in documentation repositories by rendering Markdown to HTML, a simple substring check on the entire output can lead to false negatives if the attribute name is preserved in explanatory HTML comments.
**Action:** Use regex or a parser to isolate the specific tag being verified in the rendered HTML to ensure the check accurately reflects the final DOM state.
