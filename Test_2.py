from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser


def get_html(page, asin):
    url = f"https://www.amazon.co.uk/dp/{asin}"
    page.goto(url)
    html = HTMLParser(page.content())
    return html

def parse_html(html, asin):
    print(html.css_first("title").text())
    print(asin)

def run():
    asin = "B08KSG27FZ"
    pw = sync_playwright().start()
    browser = pw.chromium.launch()
    page = browser.new_page()
    html = get_html(page, asin)
    parse_html(html, asin)

def main():
    run()

if __name__ == "__main__":
    main()


#https://www.amazon.co.uk/Yale-SV-DPFX-B-Detection-Privacy-Viewing/dp/B08KSG27FZ?ref_=Oct_DLandingS_D_080c2ad3_5&th=1