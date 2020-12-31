import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.servis.com/product-category']
    start_urls = ['http://www.servis.com/product-category/men']

    def parse(self, response):
        pass
