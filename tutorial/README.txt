This folder and all subfolders include code and the coding structure used by the
Scrapy python module. This extra module was used to scrape website data and form 
the relevant web content into JSON files, which are used by the program in 
creating the controlled vocabularies implemented within the solution.

Each JSON file is created by a specific web spider (found in 
tutrial\turorial\spider). Many of these spiders contain similar code - which 
reflects our use of https://www.thewhiskyexchange.com/ as a source for compelte 
lists of specific alcohol brand names. vodka_spider.py contains annotations to 
explain the code used - the other spiders use the same code structure, tailored 
for the specific web page to be scraped.

To increase the efficiency of our code, web scraped data is already saved by the 
program, rather than scraped with each individual controlled vocabulary call.

Full documentation for the Scrapy module can be found at:
http://doc.scrapy.org/en/latest/