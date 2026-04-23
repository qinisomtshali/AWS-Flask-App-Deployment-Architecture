# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality, significantly reducing LCP.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis before assuming they are fully optimized.

## 2025-04-14 - Documentation-Only Repository Constraints
**Learning:** When a repository is documentation-centric, performance wins are limited to static asset delivery and browser hints. However, generic optimizations like `fetchpriority` may be perceived as low-impact or susceptible to platform sanitization.
**Action:** Always verify visual assets using Base64 injection in Playwright when local file paths are restricted, ensuring verification screenshots accurately reflect the rendered state.
