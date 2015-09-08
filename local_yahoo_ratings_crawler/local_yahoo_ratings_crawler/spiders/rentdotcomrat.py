from scrapy.spiders import Spider
from scrapy.selector import Selector

from local_yahoo_ratings_crawler.items import LocalYahooRatingsCrawlerItem


class RentratSpider(Spider):
    name = "rentdotcomrat"
    allowed_domains = ["rent.com"]
    start_urls = [
        'http://www.rent.com/california/san-jose-apartments/colonnade-4-435135',
    ]

    def parse(self, response):
        
        items = []
        review_part1= []
        review_part2=[]
        full_review= []
        users = response.xpath('//div[@id="ratings-and-reviews"]/div[@id="individual-reviews"]/div[@class="individual-review clearfix"]')


        
        for user in users:

            item = LocalYahooRatingsCrawlerItem()
            item['username']    = user.xpath('div[@class="resident-info"]/h3/span[@itemprop="author"]/text()').extract()
            item['user_rating'] =user.xpath('div[@class="ratings-section"]/div[@class="overall-user-satisfaction"]/meta/@content').extract()
            #print "\n",item['user_rating']
            item['review_date'] =user.xpath('div[@class="review-section"]/p[@class="review-text minimize"]/span[@class="review-date"]/text()').extract()
            #print "\n",item['rating_date']
            review_part1 =user.xpath('div[@class="review-section"]/p[@class="review-text minimize"]/span[@class="blurb"]/text()').extract()
            review_part2 =user.xpath('div[@class="review-section"]/p[@class="review-text minimize"]/span[@class="remainder"]/text()').extract()
            #print review_part1,review_part2,"------->"
            temp_str     = ''.join(review_part1+review_part2)
            full_review  =[temp_str] 
            #review=list(review)
            #review.append(user.xpath('div[@class="review-section"]/p[@class="review-text minimize"]/span[@class="remainder"]').extract())
            
            item['user_review'] =full_review
            #print "\n",item['user_review']
            items.append(item)

        return items