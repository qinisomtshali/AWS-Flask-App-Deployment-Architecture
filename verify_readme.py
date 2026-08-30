import markdown
import os
from playwright.sync_api import sync_playwright

def verify():
    # 1. Read README.md
    with open('README.md', 'r') as f:
        md_content = f.read()

    # 2. Render to HTML
    html_content = markdown.markdown(md_content, extensions=['extra'])

    # 3. Create a temporary HTML file for Playwright
    html_file = '/home/jules/verification/readme.html'
    with open(html_file, 'w') as f:
        f.write(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: sans-serif; max-width: 800px; margin: auto; padding: 20px; }}
                img {{ max-width: 100%; height: auto; border: 1px solid #ccc; }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """)

    # 4. Use Playwright to take screenshot
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # Copy image to verification dir so it can be loaded
        import shutil
        shutil.copy('architecture-diagram.webp', '/home/jules/verification/architecture-diagram.webp')

        page.goto(f'file://{html_file}')

        # Take screenshot
        screenshot_path = '/home/jules/verification/verification.png'
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify()
