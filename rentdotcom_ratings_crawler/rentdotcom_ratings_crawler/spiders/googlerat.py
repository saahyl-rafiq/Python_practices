from time import sleep

from scrapy import Spider, Request, Selector

from selenium import webdriver
from rentdotcom_ratings_crawler.items import RentdotcomRatingsCrawlerItem


class GoogleSpider(Spider):
    name = 'google'
    # allowed_domains = ['']
    start_urls = [
                  'https://plus.google.com/100941404362113740925/about?hl=en',
                  #'https://plus.google.com/+CopperCreekApartmentsLasVegas/about?hl=en',
                  'https://plus.google.com/+GovernorsRidgeApartmentsPittsburgh/about',

    ]
    items = []

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.getsel(response)
        return self.items

    def getsel(self,response):
        self.driver.get(response.url)
        isdisp = self.driver.find_element_by_xpath('//span[@class="d-s L5 r0"]').is_displayed()
        if isdisp:
            #users = response.xpath('//span[@class="d-s L5 r0"]')
            #for ck in users:
            next = self.driver.find_element_by_xpath('//span[@class="d-s L5 r0"]')
            next.click()
            selen_html = self.driver.page_source
            hxs = Selector(text=selen_html)
            sleep(5)
            selen_html = self.driver.page_source
            hxs = Selector(text=selen_html)
            self.parse_second(hxs)
            #self.driver.close()
        else:
            self.parse_second(response)
            #self.driver.close()


    def parse_second(self, response):
        print 'you are here!'
        response = response.xpath('//div[@class="ojb"]')
        for user in response:
            item = RentdotcomRatingsCrawlerItem()
            username = user.xpath('span[@class="Gl aCb Khb"]/a/text()').extract()
            if not username:
                item['username'] = user.xpath('span[@class="Gl aCb Mlc"]/text()').extract()
            else:
                item['username'] = username
            item['user_rating'] = len(user.xpath('div/div/span[@class="b-db-ac b-db-ac-th"]').extract())
            item['review_date'] = user.xpath('div/div/span[@class="VUb"]/text()').extract()
            item['user_review'] = user.xpath('div/div/span[@class="GKa oAa"]/text()').extract()
            #item['crawl_site'] = 'google'
            self.items.append(item)

