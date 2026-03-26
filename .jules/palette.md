## 2025-01-24 - Accessible Complex Diagrams
**Learning:** Architecture diagrams with generated text are often unreadable by screen readers and can be difficult for human users if text is small. Using a concise `alt` attribute that points to detailed, structured text sections (e.g., 'See the Core Components section...') creates a much better UX than long alt-text or no description.
**Action:** For every complex technical illustration, provide a corresponding markdown section (using headings and lists) that describes the same information and link to it in the image's `alt` text.
