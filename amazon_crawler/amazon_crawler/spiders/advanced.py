from gc import callbacks
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AmazonCrawlerItem

class AdvancedSpider(CrawlSpider):
    name = 'advanced'
    allowed_domains = ['amazon.com']
    page_number = 2

    # for url in start_urls:
    #     yield scrapy.Request(url=url, callback=self.parse_item)
    def start_requests(self):
        start_urls = ['https://www.amazon.com/s?k=gaming+headsets&pd_rd_r=36dc48bd-7fad-49d3-ac92-222fe4fe5be5&pd_rd_w=J7m4j&pd_rd_wg=ZAQQK&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=ZFX51PCD7D5QWEF90KR9&ref=pd_gw_unk']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse_item)
    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )



    def parse_item(self, response):

        title = response.css('.a-size-medium::text').extract()
        number_of_rating = response.css('.s-link-style .s-underline-text::text').extract()
        price_whole = response.css('.a-text-price span::text').extract()
        offer = response.css('.a-price-whole::text').extract()

        for des, wholePrice, ratingcount, num in zip(title, price_whole, number_of_rating, offer):
            try:
                item = AmazonCrawlerItem()
                item['product_name'] = des
                item['product_rating_count'] = wholePrice
                item['product_cost_actucal'] = ratingcount
                item['product_cost_offer'] = num
            except Exception as e:
                print(e)
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
            yield item

        
        next_page = "https://www.amazon.com/s?k=gaming+headsets&page="+str(AdvancedSpider.page_number)+"&pd_rd_r=36dc48bd-7fad-49d3-ac92-222fe4fe5be5&pd_rd_w=J7m4j&pd_rd_wg=ZAQQK&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=ZFX51PCD7D5QWEF90KR9&qid=1644770182&ref=sr_pg_2"
        if AdvancedSpider.page_number <=20:
            AdvancedSpider.page_number+=1
            yield response.follow(next_page, callback = self.parse_item)
        