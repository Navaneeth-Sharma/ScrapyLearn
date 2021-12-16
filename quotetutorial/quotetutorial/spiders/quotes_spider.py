import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes' # Name of the spider to reference in the command line
    start_urls = [
        'http://quotes.toscrape.com/', # start_urls is a list of urls to scrape
    ]

    def parse(self, response):
        # Extracting the quotes from the response 
        
        title = response.css('title::text').extract() # extract the title of the page and store it in a list 
        # here ::text is a css selector that extracts the text from the title tag
        yield {'titletext': title} # yield is a keyword that sends the data to the pipeline

    