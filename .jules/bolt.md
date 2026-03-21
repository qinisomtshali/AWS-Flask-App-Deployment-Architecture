## 2026-03-21 - [C2PA Metadata Stripping]
**Learning:** WebP images containing Content Provenance (C2PA) or XMP metadata can carry significant overhead (often >100KB); stripping these RIFF chunks manually is 100% lossless as it bypasses VP8/VP8L re-encoding.
**Action:** Always inspect large WebP assets for unnecessary metadata chunks before considering lossy compression or resolution changes.
