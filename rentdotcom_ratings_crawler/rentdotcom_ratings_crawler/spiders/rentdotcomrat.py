from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request, Response

from rentdotcom_ratings_crawler.items import RentdotcomRatingsCrawlerItem


class RentratSpider(Spider):
    name = "rentdotcomrat"
    allowed_domains = ["rent.com"]
    start_urls = [
        #'http://www.rent.com/minnesota/minneapolis-apartments/new-boston-square-apartments-4-438999'
        'http://www.rent.com/minnesota/minneapolis-apartments/new-boston-square-apartments-reviews-5-438999'
   
    ]



    def parse(self, response):

        for i in range(1,10):
            url=response.url+'?page='+str(i)
            yield Request(url,callback=self.parse_listings)
    

    def parse_listings(self, response):
        
        #if response.xpath('//div[@class="individual-review clearfix"]'):
        items = []
        review_part1= []
        review_part2=[]
        full_review= []
        users = response.xpath('//div[@id="ratings-and-reviews"]/div[@id="individual-reviews"]/div[@class="individual-review clearfix"]')
        ppt=response.xpath('//header[@class="ratings-prop-header clearfix"]/h1/text()').extract()
        uppt=''.join(ppt)
        sppt=uppt.encode('utf-8')
        prop=sppt[:-40]
  
        for user in users:

            item = RentdotcomRatingsCrawlerItem()

            item['property_name']    = prop
            item['username']         = user.xpath('div[@class="resident-info"]/h3/span[@itemprop="author"]/text()').extract()
            item['user_rating']      = user.xpath('div[@class="ratings-section"]/div[@class="overall-user-satisfaction"]/meta/@content').extract()
            item['review_date']      = user.xpath('div[@class="review-section"]/p[@class="review-text minimize"]/span[@class="review-date"]/text()').extract()

            review_part1 =user.xpath('div[@class="review-section"]/p[@class="review-text minimize"]/span[@class="blurb"]/text()').extract()
            review_part2 =user.xpath('div[@class="review-section"]/p[@class="review-text minimize"]/span[@class="remainder"]/text()').extract()
            temp_str     = ''.join(review_part1+review_part2)
            full_review  =[temp_str]             
            item['user_review']      = full_review

            items.append(item)

        return items
