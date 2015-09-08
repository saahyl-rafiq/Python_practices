from scrapy.spiders import Spider
from scrapy.selector import Selector

from yellowpages_ratings_crawler.items import YellowpagesRatingsCrawlerItem


class YellowratSpider(Spider):
    name = "yellowpagesrat"
    allowed_domains = ["yellowpages.com"]
    start_urls = [
        'http://www.yellowpages.com/aurora-co/mip/the-fairways-at-lowry-462091617',
    ]

    def parse(self, response):
        
        items = []

        users = response.xpath('//div[@id="reviews-container"]/article[@class="clearfix"]/div[@class="entry clearfix"]')
        prop = response.xpath('//div[@class="business-card clearfix"]/h1/text()').extract()


        for user in users:

            item = YellowpagesRatingsCrawlerItem()
            item['property'] = prop
            item['username'] = user.xpath('a[@class="author"]/text()').extract()
            item['user_rating'] = user.xpath('div[@itemprop="reviewRating"]/div[@class="result-rating one "]/meta/@content').extract()
            #print "\n",item['user_rating']
            item['review_date'] = user.xpath('span[@class="date-posted"]/text()').extract()
            #print "\n",item['rating_date']
            item['user_review'] = user.xpath('p[@class="review-response"]/text()').extract()
            #print "\n",item['user_review']
            items.append(item)

        return items