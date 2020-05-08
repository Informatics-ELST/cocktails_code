#https://en.wikipedia.org/wiki/List_of_vodkas

import scrapy


#This commented out function was used to download the html code for the webpage to aid with selecting the variables to slect to scrape the desired data
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


class VodkaSpider(scrapy.Spider):
    name = "vodka" #name used to call the spider

    #URL(s) to be scraped
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_vodkas',
    ]

    #The below line was used to isolate the desired data in the Scrapy shell
    #response.css('tr td:nth-child(1) a::text').getall()

    #This code parses the scraped data to output the desired data - specified by its CSS tags
    def parse(self, response):
        for vodka in response.css('tr td:nth-child(1)'):
            yield {
                'vodka_brand': vodka.css('a::text').get(),

            }
