## 2026-03-11 - Metadata Bloat in Provenance-Signed Images
**Learning:** Images (like WebP) can contain large `C2PA` (Content Provenance and Authenticity) metadata chunks that significantly increase file size (~140KB in this case, or 28% of the file) without contributing to visual quality. Standard image libraries might not be available in all environments to strip this.
**Action:** Always inspect large binary assets for unnecessary metadata chunks (RIFF tags like 'XMP ', 'EXIF', or 'C2PA') when optimizing for bandwidth. Use byte-level manipulation if specialized tools are missing.
