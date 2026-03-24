## 2024-03-24 - AI-generated WebP Metadata Optimization
**Learning:** AI-generated images (like those from DALL-E) often contain significant metadata overhead (C2PA, XMP) that can be stripped losslessly without re-encoding the bitstream.
**Action:** Always check WebP assets for large non-VP8 chunks and strip them to reduce file size while maintaining pixel-perfect quality.
