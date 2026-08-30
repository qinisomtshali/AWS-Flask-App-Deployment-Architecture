# Bolt's Journal - Critical Learnings

## 2025-03-26 - Documentation Performance
**Learning:** In documentation-only repositories, image assets are the primary performance bottleneck. Successive rounds of optimization (e.g., reducing WebP Quality from 80 to 70 with Method 6 effort) can still yield ~18% gains without perceptible loss. AI-generated images often contain large metadata chunks (like C2PA) that should be stripped first.
**Action:** Use high-effort (Method 6) re-encoding at Quality 70-80 for LCP candidates. Always verify with automated screenshots to ensure visual parity.
