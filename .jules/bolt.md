## 2025-05-24 - WebP Metadata Overhead
**Learning:** AI-generated WebP documentation assets can carry significant (~28% or more) overhead in the form of C2PA (Content Provenance) and XMP metadata chunks. This metadata is not required for rendering and can be stripped losslessly at the binary level without touching the VP8/VP8L bitstream.
**Action:** When working with documentation-heavy repositories, always check for non-essential RIFF chunks in WebP images. Use custom scripts to strip these for significant LCP improvements without sacrificing image quality.
