## 2026-03-03 - Documentation Image Optimization
**Learning:** In documentation-heavy repositories, the documentation itself is the UI. Using standard Markdown image syntax for large diagrams without explicit dimensions causes significant Cumulative Layout Shift (CLS). Renaming assets with special characters (like DALL-E defaults) to kebab-case also avoids potential shell/path resolution issues.
**Action:** Always prefer <img> tags over Markdown syntax for large documentation images to enable width/height attributes, async decoding, and eager loading strategies.
