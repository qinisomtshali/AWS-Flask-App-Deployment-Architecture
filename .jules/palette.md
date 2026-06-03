## 2025-05-15 - AI-Generated Diagram Accessibility
**Learning:** AI-generated diagrams (like the architecture visualization) often contain text artifacts or typos that can be difficult for all users to read. For screen reader accessibility and general clarity, it's essential to provide a comprehensive text-based alternative within the documentation rather than relying solely on the `alt` attribute for complex details.
**Action:** When documenting architecture with complex images, include "Core Components" and "Deployment Workflow" text sections and link to them in the image `alt` text (e.g., 'See the Core Components section for a detailed description').

## 2026-06-03 - Diagram-to-Text Information Parity
**Learning:** Large diagrams in documentation require tight parity with text descriptions. When components are visually represented in a diagram but missing from the explanatory text (e.g., Security Groups, Subnets), it creates an accessibility gap. Adding direct anchor links from visual assets to their detailed textual descriptions significantly improves navigation for users wanting immediate details.
**Action:** Audit complex diagrams against their accompanying text to ensure all visual elements are described. Use internal anchor links in figure captions to bridge visual assets and detailed documentation sections.
