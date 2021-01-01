import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        page_title = response.xpath("//div[@class='page-header action']/h1/text()").get()
        lists = response.xpath("//ol[@class='row']/li/article")
        for data in lists:
            tags = data.xpath(".//div/a")
            image_src = tags.css('img').attrib['src']
            yield {
                'title': page_title,
                'image_src': image_src
            }
