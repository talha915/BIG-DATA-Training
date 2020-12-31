import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.servis.com/product-category']
    start_urls = ['http://www.servis.com/product-category/men']

    def parse(self, response):
        titles = response.xpath("//div[@class='box-text box-text-products']/div[@class='title-wrapper']/p[@class='name product-title']/a")

        for title in titles:
            product_title = title.xpath(".//text()").get()
            yield {
                'title': product_title
            }