# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. AI-generated images often contain large metadata chunks (like C2PA) that can be stripped without affecting visual quality. If metadata stripping isn't enough, lossy re-encoding (Quality 80) can provide a significant LCP boost (~41% reduction) with negligible visual impact.
**Action:** Always check WebP/PNG assets for metadata chunks using binary analysis. If stripping is insufficient, use Pillow for high-effort lossy re-encoding to optimize for LCP.

## 2026-06-17 - WebP Optimization for Documentation
**Learning:** Successive rounds of optimization for documentation assets (e.g., reducing WebP quality from 80 to 70) can still yield meaningful performance gains (~18% in this case) without noticeable quality loss on technical diagrams.
**Action:** Re-evaluate "already optimized" assets if LCP is still a concern; further compression may be possible without sacrificing clarity.
