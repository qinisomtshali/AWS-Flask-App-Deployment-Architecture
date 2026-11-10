# Bolt's Journal - Critical Learnings

## 2025-05-18 - Successive WebP Compression Tuning
**Learning:** Re-evaluating previously optimized WebP images (Quality 80) with a slightly more aggressive quality target (Quality 70, Method 6) can yield double-digit percentage gains (~18% size reduction, saving ~37KB) without perceptible visual degradation or text artifacting in complex technical diagrams.
**Action:** When inspecting documentation assets that appear already optimized, test compression steps around Quality 70 with Method 6 while verifying legibility with read_image_file.

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.
