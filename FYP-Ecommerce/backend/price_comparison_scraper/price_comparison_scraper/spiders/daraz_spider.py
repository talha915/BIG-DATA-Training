import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse
import time


class DarazSpider(scrapy.Spider):
    name = "daraz"
    start_urls = ["https://www.daraz.pk/catalog/?q=iphone"]

    def __init__(self, *args, **kwargs):
        super(DarazSpider, self).__init__(*args, **kwargs)

        # Chrome options set karna
        chrome_options = Options()
        chrome_options.add_argument(
            "--headless"
        )  # Browser ko visible nahi karne ke liye
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # ChromeDriver ka path specify karna (agar path system path me add nahi kiya)
        self.driver = webdriver.Chrome(
            service=Service("/path/to/chromedriver"), options=chrome_options
        )

    def parse(self, response):
        # Selenium ke through page load karna
        self.driver.get(response.url)
        time.sleep(
            2
        )  # Wait karna until page load ho jaye (aap condition bhi laga sakte hain)

        # Selenium ke response ko Scrapy format me convert karna
        selenium_response = HtmlResponse(
            url=self.driver.current_url, body=self.driver.page_source, encoding="utf-8"
        )

        # Yahan aap page scrape kar sakte hain
        products = selenium_response.xpath(
            '//div[@class="_17mcb"]//div[@class="Bm3ON"]'
        )
        for product in products:
            product_title = product.xpath('.//div[@class="RfADt"]/a/@title').get()
            product_price = product.xpath(
                './/div[@class="aBrP0"]/span[@class="ooOxS"]/text()'
            ).get()
            product_url = product.xpath('.//div[@class="RfADt"]/a/@href').get()
            product_image_url = product.xpath(".//img/@src").get()

            yield {
                "title": product_title,
                "price": product_price,
                "url": response.urljoin(product_url),
                "image_url": product_image_url,
            }

    def closed(self, reason):
        # Browser close karna jab scraping complete ho jaye
        self.driver.quit()
