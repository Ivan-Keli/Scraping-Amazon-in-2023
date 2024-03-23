from playwright.sync_api import sync_playwright
from dataclasses import dataclass
from selectolax.parser import HTMLParser


@dataclass
class Item:
    asin: str
    title: str
    price: str

def get_html(page, asin):
    url = f"https://www.amazon.co.uk/dp/{asin}"
    page.goto(url)
    return page.content()

def parse_html(content, asin):
    html = HTMLParser(content)
    item = Item(
        asin=asin,
        title=html.css_first("span#productTitle").text(strip=True),
        price=html.css_first("span.a-offscreen").text(strip=True)
    )
    return item

def run():
    asin = "B08KSG27FZ"
    pw = sync_playwright().start()
    browser = pw.chromium.launch()
    page = browser.new_page()
    html_content = get_html(page, asin)
    product = parse_html(html_content, asin)
    print(product)

def main():
    run()


if __name__ == "__main__":
    main()
