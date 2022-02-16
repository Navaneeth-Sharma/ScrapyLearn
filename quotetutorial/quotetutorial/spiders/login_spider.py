import scrapy
from scrapy.http import FormRequest


class LoginSpiderSpider(scrapy.Spider):

    name = 'login_spider'
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': csrf_token,
            'username': 'coool',
            'password': 'wedfwfs'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        print("DONE")
