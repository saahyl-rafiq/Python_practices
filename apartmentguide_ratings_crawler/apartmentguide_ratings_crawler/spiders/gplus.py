from scrapy.selector import Selector
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request, FormRequest

from apartmentguide_ratings_crawler.items import ApartmentguideRatingsCrawlerItem


class LoginSpider(CrawlSpider):
    name = 'loginrat'    
    start_urls = ['https://mail.google.com/']

    def parse(self, response):
        return [FormRequest.from_response(response,
                    formdata={'Email': 'saahylrafiq', 'Passwd': ''},
                    callback=self.after_login)]

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.log("Login failed", level=log.ERROR)
        elif "Hi Saahyl" in response.body:

            self.log("Successfully logged in. Let's start crawling!")
            print "####################################################"

            return