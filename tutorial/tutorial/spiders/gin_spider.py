#https://www.thewhiskyexchange.com/brands/spirits/338/gin

import scrapy


"""class GinSpider(scrapy.Spider):
    name = "Gin"

    def start_requests(self):
            urls = [
                'https://www.thewhiskyexchange.com/brands/spirits/338/gin',
            ]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
            #page = response.url.split("/")[-2]
            #filename = 'quotes-%s.html' % page
            filename = 'Gin.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)"""

class GinSpider(scrapy.Spider):
    name = "Gin"
    start_urls = [
        'https://www.thewhiskyexchange.com/brands/spirits/338/gin'
    ]

    #response.css('.az-item-name::text').getall()
    def parse(self, response):
        for Gin in response.css('.az-item-name'):
            yield {
                'Gin_brand': Gin.css('::text').get(),

            }