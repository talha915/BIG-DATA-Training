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
            image_alt = tags.css('img').attrib['alt']
            url_link = tags.xpath(".//@href").get()
            ratings = data.xpath(".//p/@class").get()
            product_title = data.xpath(".//h3/a/@title").get()
            product_price = data.xpath(".//div[@class='product_price']/p[@class='price_color']/text()").get()
            yield {
                'page_title': page_title,
                'product_title': product_title,
                'product_image_path': image_src,
                'product_image_attribute': image_alt,
                'product_link': url_link,
                'product_rating': ratings,
                'product_price': product_price
            }
