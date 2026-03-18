# Bolt's Journal - Critical Performance Learnings

## 2025-03-18 - Metadata Overhead in Documentation Assets
**Learning:** WebP images containing Content Provenance (C2PA) metadata can carry significant overhead (over 100KB) that doesn't contribute to visual quality. Stripping these RIFF chunks is a lossless way to reduce documentation asset size.
**Action:** Always check for and remove unnecessary metadata chunks like `C2PA` from WebP assets to improve documentation load times and repository efficiency.
