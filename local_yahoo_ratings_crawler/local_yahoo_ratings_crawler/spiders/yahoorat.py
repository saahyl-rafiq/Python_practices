from scrapy.spiders import Spider
from scrapy.selector import Selector

from local_yahoo_ratings_crawler.items import LocalYahooRatingsCrawlerItem


class YahooratSpider(Spider):
    name = "yahoorat"
    allowed_domains = ["local.yahoo.com/"]
    start_urls = [
        'https://local.yahoo.com/info-18716015-skyline-place-apartments-dallas/',
    
    ]

    def parse(self, response):
        
        items = []
        review = []
        #users = response.xpath('//div[@class="info-reviews"]//div[@class="review-head"]')
        users = response.xpath('//div[@class="info-reviews"]/ul[@class="uil"]/li')


        #for site in sites:
        #item = LocalYahooRatingsCrawlerItem()
        #item['entity_title']= response.xpath('//h1[@class="kg-style1 top-pad"]/text()').extract()
        #print item['entity_title']
        #item['entity_type'] = response.xpath('//div[@class="info-biz-card"]//h2[@class="kg-style2"]/span/a/text()').extract()
        #print "\n",item['entity_type']
        for user in users:

            item = LocalYahooRatingsCrawlerItem()
            #item['username']    = user.xpath('strong/text()').extract()
            item['username']    = user.xpath('div[@class="review-head"]/strong/text()').extract()
            #print "\n", item['username']
            #item['user_rating'] = user.xpath('span/@data-value').extract()
            item['user_rating'] =user.xpath('div[@class="review-head"]/span[@class="yahoo-sprite rating small"]/@data-value').extract()
            #print "\n",item['user_rating']
            item['review_date'] =user.xpath('div[@class="review-head"]/em/text()').extract()
            #print "\n",item['rating_date']
            #review =response.xpath('//div[@class="info-reviews"]//p[@itemprop="reviewBody"]/span/text()').extract()
            review =user.xpath('p[@itemprop="reviewBody"]/span/text()').extract()
            if not review:
                #review = response.xpath('//div[@class="info-reviews"]//p[@itemprop="reviewBody"]/text()').extract()
                review =user.xpath('p[@itemprop="reviewBody"]/text()').extract()
            

            item['user_review'] = review
            #print "\n",item['user_review']
            items.append(item)

        return items