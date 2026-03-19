## 2024-05-15 - Lossless WebP Metadata Stripping (C2PA)

**Learning:** WebP images containing Content Provenance (C2PA) metadata can carry significant overhead (often >100KB) within a 'c2pa' RIFF chunk. This metadata is separate from the image data (VP8/VP8L chunks) and can be stripped at the binary level without re-encoding, resulting in a 100% lossless size reduction.

**Action:** Before resorting to lossy compression for WebP documentation assets, always inspect the RIFF chunks for large metadata blocks like 'c2pa' or 'XMP ' and strip them first to preserve maximum visual fidelity while reducing payload.
