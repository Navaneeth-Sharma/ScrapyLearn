import scrapy


class AmazonCrawlerItem(scrapy.Item):

    # Primary fields
    product_name = scrapy.Field()
    product_cost = scrapy.Field()
    product_rating_count = scrapy.Field()
    product_cost_actucal = scrapy.Field()
    product_cost_offer = scrapy.Field()

    # Housekeeping Fields
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    date = scrapy.Field()
