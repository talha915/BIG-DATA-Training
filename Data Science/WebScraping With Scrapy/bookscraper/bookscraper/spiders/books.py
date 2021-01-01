import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        page_title = response.xpath("//div[@class='page-header action']/h1/text()").get()

        yield {
            'title': page_title
        }
