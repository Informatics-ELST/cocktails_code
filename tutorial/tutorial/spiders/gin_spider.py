#https://en.wikipedia.org/wiki/List_of_vodkas

import scrapy


"""class GinSpider(scrapy.Spider):
    name = "gin"

    def start_requests(self):
            urls = [
                'https://www.thewhiskyexchange.com/brands/spirits/338/gin',
            ]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
            #page = response.url.split("/")[-2]
            #filename = 'quotes-%s.html' % page
            filename = 'gin.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)"""

class GinSpider(scrapy.Spider):
    name = "gin"
    start_urls = [
        'https://www.thewhiskyexchange.com/brands/spirits/338/gin',
    ]

    #response.css('az-item-name a::text').getall()
    def parse(self, response):
        for gin in response.css('az-item-name'):
            yield {
                'gin_brand': gin.css('a::text').get(),

            }