#https://www.thewhiskyexchange.com/brands/scotchwhisky/40/single-malt-scotch-whisky

import scrapy


"""class WhiskySpider(scrapy.Spider):
    name = "whisky"

    def start_requests(self):
            urls = [
                'https://www.thewhiskyexchange.com/brands/scotchwhisky/40/single-malt-scotch-whisky',
            ]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
            #page = response.url.split("/")[-2]
            #filename = 'quotes-%s.html' % page
            filename = 'whisky.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)"""

class QuotesSpider(scrapy.Spider):
    name = "whisky"
    start_urls = [
        'https://www.thewhiskyexchange.com/brands/scotchwhisky/40/single-malt-scotch-whisky',
        'https://www.thewhiskyexchange.com/brands/scotchwhisky/304/blended-scotch-whisky',
        'https://www.thewhiskyexchange.com/brands/scotchwhisky/309/blended-malt-scotch-whisky',
        'https://www.thewhiskyexchange.com/brands/scotchwhisky/310/grain-scotch-whisky',
    ]

    #response.css('.az-item-name::text').getall()
    def parse(self, response):
        for whisky in response.css('.az-item-name'):
            yield {
                'whisky_brand': whisky.css('::text').get(),

            }
