#https://en.wikipedia.org/wiki/List_of_vodkas

import scrapy


"""class VodkaSpider(scrapy.Spider):
    name = "vodka"

    def start_requests(self):
            urls = [
                'https://en.wikipedia.org/wiki/List_of_vodkas',
            ]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
            #page = response.url.split("/")[-2]
            #filename = 'quotes-%s.html' % page
            filename = 'vodka.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)"""

class QuotesSpider(scrapy.Spider):
    name = "vodka"
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_vodkas',
    ]

    #response.css('tr td:nth-child(1) a::text').getall()
    def parse(self, response):
        for vodka in response.css('tr td:nth-child(1)'):
            yield {
                'vodka_brand': vodka.css('a::text').get(),

            }
