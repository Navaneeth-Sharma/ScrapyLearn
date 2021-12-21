import scrapy
from ..items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'  # Name of the spider to reference in the command line
    start_urls = [
        'http://quotes.toscrape.com/',  # start_urls is a list of urls to scrape
    ]

    def parse(self, response):

        # # Extracting the quotes from the response
        # # extract the title of the page and store it in a list
        # # here ::text is a css selector that extracts the text from the title tag
        # title = response.css('title::text').extract()
        # # yield is a keyword that sends the data to the pipeline
        # yield {'titletext': title}

        items = QuotetutorialItem()

        all_dic_quotes = response.css('div.quote')

        for quote in all_dic_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('small.author::text').extract()
            tags = quote.css('div.tags a.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            yield items

        next_page = response.css("li.next a::attr(href)").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

        # # Extracting the quotes from the response