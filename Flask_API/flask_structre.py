# from flask import Flask

# app = Flask(__name__)   # object creation

# @app.route('/')     #syntax
# def hello():
#     return "Hello gen ai programme"

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, jsonify
from playwright.async_api import async_playwright
import asyncio

app = Flask(__name__)


async def run_playwright():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://example.com")

        title = await page.title()

        await browser.close()
        return title


@app.route("/")
def home():
    return "Flask + Playwright is running!"


@app.route("/run-test")
def run_test():
    result = asyncio.run(run_playwright())
    return jsonify({
        "message": "Playwright executed successfully",
        "page_title": result
    })


if __name__ == "__main__":
    app.run(debug=True)