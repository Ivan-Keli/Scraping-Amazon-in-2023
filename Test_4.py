from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from dataclasses import dataclass
from rich import print
import csv


@dataclass
class Item:
    asin: str
    title: str
    price: str

def get_html(page, asin):
    url = f"https://www.amazon.co.uk/dp/{asin}"
    page.goto(url, timeout=60000)  # Set timeout to 60 seconds (60000 milliseconds)
    html = HTMLParser(page.content())
    return html

def parse_html(html, asin):
    item = Item(
        asin=asin,
        title=html.css_first("span#productTitle").text(strip=True),
        price=html.css_first("span.a-offscreen").text(strip=True)
    )
    return item

def read_csv():
    csv_file_path = 'C:/Users/ivank/Downloads/Modern Web Scrapping with Python/Scraping Amazon in 2023/products.csv'
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        return [item[0] for item in reader]

def run(asin):
    pw = sync_playwright().start()
    browser = pw.chromium.launch()
    page = browser.new_page()
    html = get_html(page, asin)
    product = parse_html(html, asin)
    print(product)
    browser.close()
    pw.stop()

def main():
    asins = read_csv()
    for asin in asins:
        run(asin)

if __name__ == "__main__":
    main()
