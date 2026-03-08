## 2025-05-15 - Documentation-as-the-App Optimization
**Learning:** In repositories serving primarily as architectural documentation, the `README.md` and its assets are the "Frontend." Standard web performance optimizations like explicit image dimensions (to prevent CLS) and `loading="eager"` for LCP assets apply even if the codebase itself doesn't have a traditional web server.
**Action:** Treat documentation assets (diagrams/screenshots) with the same performance rigor as application assets: use modern formats (WebP), explicit sizing, and strategic loading/decoding attributes.
