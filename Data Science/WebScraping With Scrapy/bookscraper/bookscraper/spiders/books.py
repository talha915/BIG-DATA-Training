import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']
    base_url = 'http://books.toscrape.com/catalogue/'
    
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
        # For Pagination   
        next_page_partial_url = response.xpath("//ul[@class='pager']/li[@class='next']/a/@href").get()
        next_page_url = self.base_url + next_page_partial_url

        yield scrapy.Request(next_page_url, callback=self.parse)
        

    def parseProductDetail(self, response):
        page_title = response.request.meta['page_title']
        product_title = response.request.meta['product_title']
        product_image_path = response.request.meta['product_image_path']
        product_image_attribute = response.request.meta['product_image_attribute']
        product_link = response.request.meta['product_link']
        product_rating = response.request.meta['product_rating']
        product_price = response.request.meta['product_price']
        stock_availability = response.request.meta['stock_availability']

        description = response.xpath("//article/p/text()").get()
        product_upc = response.xpath("(//table[@class='table table-striped'])[1]/tr[1]/td/text()").get()
        product_type = response.xpath("(//table[@class='table table-striped'])[1]/tr[2]/td/text()").get()
        product_price_exclusive = response.xpath("(//table[@class='table table-striped'])[1]/tr[3]/td/text()").get()
        product_price_inclusive = response.xpath("(//table[@class='table table-striped'])[1]/tr[4]/td/text()").get()
        product_tax = response.xpath("(//table[@class='table table-striped'])[1]/tr[5]/td/text()").get()
        stock_availability = response.xpath("(//table[@class='table table-striped'])[1]/tr[6]/td/text()").get()
        reviews = response.xpath("(//table[@class='table table-striped'])[1]/tr[7]/td/text()").get()
        yield {
            'page_title': page_title,
            'product_title': product_title,
            'product_image_path': product_image_path,
            'product_image_attribute': product_image_attribute,
            'product_link': product_link,
            'product_rating': product_rating,
            'product_price': product_price,
            'product_description': description,
            'product_upc': product_upc,
            'product_type': product_type,
            'product_price_exclusive_tax': product_price_exclusive,
            'product_price_inclusive_tax': product_price_inclusive,
            'tax_on_product': product_tax,
            'product_availability': stock_availability,
            'product_review': reviews
        }        
