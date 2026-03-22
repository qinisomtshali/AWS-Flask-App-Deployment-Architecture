## 2025-03-22 - Lossless Metadata Stripping for WebP Assets
**Learning:** Large AI-generated WebP images often contain significant metadata (C2PA, XMP) that is not required for web rendering. In this case, removing the 'c2pa' RIFF chunk reduced the file size by ~137KB (28.5%) without any loss in image quality, as it avoids re-encoding the VP8/VP8L bitstream.
**Action:** Always profile image assets for non-essential metadata chunks before considering lossy re-compression. Stripping metadata is 100% safe and yields immediate performance gains for LCP.
