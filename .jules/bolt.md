# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2026-05-07 - Documentation-only Repositories and Measurement
**Learning:** In repositories containing only documentation, "application performance" translates to "documentation loading performance." Optimizations like image compression must be accompanied by in-file comments to ensure they aren't accidentally reverted by future edits.
**Action:** Always document asset-level optimizations directly in the source file (e.g., HTML/Markdown comments) and include precise measurement metrics (original vs. optimized size) in the PR and journal.
