import scrapy
import logging

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")

        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            yield response.follow(url = link, callback = self.parseCountry, meta={'country_name': name})

    def parseCountry(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")

        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            pop = row.xpath(".//td[2]/strong/text()").get()
            yearly_change = row.xpath(".//td[4]/text()").get()

            yield {
                'country_names': name,
                'year': year,
                'country_population': pop,
                'yearly_change': yearly_change
            }        
