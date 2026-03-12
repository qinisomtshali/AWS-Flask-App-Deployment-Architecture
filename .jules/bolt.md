# Bolt's Journal - Critical Learnings Only

## 2025-03-12 - Stripping C2PA Metadata from Documentation Assets
**Learning:** High-resolution design assets (WebP/PNG) often contain significant "hidden" payload bloat in the form of C2PA (Content Provenance) metadata, which can exceed 100KB without affecting visual quality. In documentation-heavy repos, this impacts repository cloning speed and initial README rendering (LCP).
**Action:** Use byte-level inspection to identify non-essential metadata chunks in assets and strip them using safe processing scripts.
