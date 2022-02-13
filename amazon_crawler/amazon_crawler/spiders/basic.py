import scrapy
# from ..items import AmazonCrawlerItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=gaming+headsets&pd_rd_r=36dc48bd-7fad-49d3-ac92-222fe4fe5be5&pd_rd_w=J7m4j&pd_rd_wg=ZAQQK&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=ZFX51PCD7D5QWEF90KR9&ref=pd_gw_unk']

    def parse(self, response):

        # items = AmazonCrawlerItem()

        print(response.css('.a-price-whole::text').extract())
        # print(response.xpath('//[@class="a-price-whole"]/text()').extract())
