from scrapy.selector import Selector
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request, Response
from scrapy.linkextractors import LinkExtractor

from rentdotcom_ratings_crawler.items import RentdotcomRatingsCrawlerItem


class RtSpider(CrawlSpider):
    name = "rentrat"
    allowed_domains = ["rent.com"]
    start_urls = [
        #'http://www.rent.com/minnesota/minneapolis-apartments/new-boston-square-apartments-4-438999',
        'http://www.rent.com/minnesota/minneapolis-apartments/new-boston-square-apartments-reviews-5-438999'

    ]

    rules = (
    #     # Extract links for next pages
    #     #Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="block-body"]//a[contains(., "See More Reviews")]')), callback='parse_listings', follow=True),
    #     #Rule(LinkExtractor(allow=(), restrict_xpaths='//div[@class="block-body"]//a[contains(., "See More Reviews")]')),
          #Rule(LinkExtractor(allow=(r'.*-reviews-5-\d\?page=\d+',), restrict_xpaths=('//div[@class="paging"]/ul/li[@class="pg-next"]/a[contains(., "Next")]')), callback='parse_listings', follow=True),
          Rule(LinkExtractor(allow=(r'/minnesota/(.*)-reviews-5-\d\?page=\d+',)), callback='parse_listings'),

    #     #Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[contains(@class, "leftright")][1]//a[contains(., "Next")]')), callback='parse_listings', follow=True),
      )


    # def parse_start_url(self, response):
    #     '''
    #     Crawl start_urls
    #     '''
    #     # #i=0
    #     # print response.url
    #     # p=len(response.xpath('//div[@class="paging"]/ul/li'))

    #     # print p

    #     #  #pages=len(response.xpath('//div[@class="paging"]/ul/li'))-2
    #     print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    #     for i in range(1,4):
    #         url=response.url+'?page='+str(i)
    #         yield Request(url,callback=self.parse_listings)
    #         #print url


    # #     #return self.parse_listings(response)
    #     return


    def parse_listings(self, response):
        
        items = []
        review_part1= []
        review_part2=[]
        full_review= []
        users = response.xpath('//div[@id="ratings-and-reviews"]/div[@id="individual-reviews"]/div[@class="individual-review clearfix"]')
        print users

        
        for user in users:

            item = RentdotcomRatingsCrawlerItem()
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