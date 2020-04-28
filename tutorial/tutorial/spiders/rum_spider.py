#https://www.thewhiskyexchange.com/brands/spirits/339/rum

import scrapy


"""class rumSpider(scrapy.Spider):
    name = "rum"

    def start_requests(self):
            urls = [
                'https://www.thewhiskyexchange.com/brands/spirits/339/rum',
            ]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
            #page = response.url.split("/")[-2]
            #filename = 'quotes-%s.html' % page
            filename = 'rum.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)"""

class RumSpider(scrapy.Spider):
    name = "rum"
    start_urls = [
        'https://www.thewhiskyexchange.com/brands/spirits/339/rum'
    ]

    #response.css('.az-item-name::text').getall()
    def parse(self, response):
        for rum in response.css('.az-item-name'):
            yield {
                'rum_brand': rum.css('::text').get(),

            }