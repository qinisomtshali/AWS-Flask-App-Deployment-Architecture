## 2025-03-15 - Stripping C2PA Metadata from WebP
**Learning:** WebP images containing Content Provenance (C2PA) metadata can contain significant overhead (often >100KB); stripping these RIFF chunks manually is 100% lossless as it bypasses VP8/VP8L re-encoding.
**Action:** Always check WebP assets for large metadata chunks (like C2PA or EXIF) when optimizing for file size, especially for AI-generated assets.
