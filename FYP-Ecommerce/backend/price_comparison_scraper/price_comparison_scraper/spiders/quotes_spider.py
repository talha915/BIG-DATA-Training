import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response):
        page_title = response.xpath('//h1/a[@style="text-decoration: none"]/text()').get()
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            quote_text = quote.xpath('.//span[@class="text"]/text()').get()
            author = quote.xpath('.//small[@class="author"]/text()').get()
            tags = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()

            yield {
                'page_title': page_title,
                'quote': quote_text,
                'author': author,
                'tags': tags
            }