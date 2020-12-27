import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        pass
