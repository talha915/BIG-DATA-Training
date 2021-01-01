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
            product_stock = data.xpath(".//div[@class='product_price']/p[2]/@class").get()
            yield response.follow(url=url_link, callback=self.parseProductDetail, 
            meta={
                'page_title': page_title,
                'product_title': product_title,
                'product_image_path': image_src,
                'product_image_attribute': image_alt,
                'product_link': url_link,
                'product_rating': ratings,
                'product_price': product_price,
                'stock_availability': product_stock
            }) 

    def parseProductDetail(self, response):
        page_title = response.request.meta['page_title']
        product_title = response.request.meta['product_title']
        product_image_path = response.request.meta['product_image_path']
        product_image_attribute = response.request.meta['product_image_attribute']
        product_link = response.request.meta['product_link']
        product_rating = response.request.meta['product_rating']
        product_price = response.request.meta['product_price']
        stock_availability = response.request.meta['stock_availability']

        yield {
            'page_title': page_title,
            'product_title': product_title,
            'product_image_path': product_image_path,
            'product_image_attribute': product_image_attribute,
            'product_link': product_link,
            'product_rating': product_rating,
            'product_price': product_price,
            'stock_availability': stock_availability
        }        
