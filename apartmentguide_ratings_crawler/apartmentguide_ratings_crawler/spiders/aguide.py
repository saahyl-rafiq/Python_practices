# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.selector import Selector
# from lxml import html
from scrapy.http import Request, Response
# from apartmentguide_ratings_crawler.items import ApartmentguideRatingsCrawlerItem
from scrapy.spiders import Spider
from scrapy.selector import Selector
import re

from apartmentguide_ratings_crawler.items import ApartmentguideRatingsCrawlerItem

class AguideSpider(Spider):
    name = "aguiderat"
    allowed_domains = ["apartmentguide.com"]
    start_urls = ['http://www.apartmentguide.com/apartments/Alabama/Huntsville/Main-Street-Apartments/45747/',
    ]


    # Request('http://www.apartmentguide.com/apartments/Alabama/Madison/Grand-Reserve-At-Madison/28587')

    # pages=len(Response.xpath('//div[@class="ld_tab_content"]/div[@id="details_ratings_reviews"]/div[@id="details_reviews"]/div[@id="reviews_container"]/div[@class="pagination"]/ol/li'))
    # print "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@",pages

    # for page in range(1,pages):
    #     start_urls.append('http://www.apartmentguide.com/apartments/Alabama/Madison/Grand-Reserve-At-Madison/28587/reviews/28587/?page=%s&sort=overallrating-desc') % page
    
    # rules = (
    #     # Extract links for next pages
    #     Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=(r'/reviews/28587/?page=2&sort=overallrating-desc')), callback='parse', follow=True),
    # )

    def parse(self, response):
        pages=len(response.xpath('//div[@class="ld_tab_content"]/div[@id="details_ratings_reviews"]/div[@id="details_reviews"]/div[@id="reviews_container"]/div[@class="pagination"]/ol/li'))
        print "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@PAGES:",pages
        #print response.url
        make_url=re.search(r'/\d+/',response.url)
        for x in range(1,pages+1):    
            #return scrapy.Request(('http://www.apartmentguide.com/apartments/Alabama/Madison/Grand-Reserve-At-Madison/28587/reviews/28587/?page=%s&sort=overallrating-desc')% x ,callback=self.parse_pages) 
            
            page_url=('http://www.apartmentguide.com/reviews%s?page=%s&sort=overallrating-desc') % (make_url.group(),x)
            print "\n###################################################",page_url
            yield Request(page_url,callback=self.parse_pages)



    def parse_pages(self, response):

        items = []

        users = response.xpath('//div[@class="review_box"]')
        #print "\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",users
        for user in users:

            item = ApartmentguideRatingsCrawlerItem()
                    
            item['username']    = user.xpath('div[@class="review_rating"]/text()').extract()
            item['user_rating'] =user.xpath('div[@class="review_rating"]/span[@itemprop="ratingValue"]/text()').extract()
            #print "\n",item['user_rating']'''
            item['review_date'] =user.xpath('p[@class="review_date"]/text()').extract()
            #print "\nreview_date: ",item['review_date']
            item['user_review'] =user.xpath('p[@itemprop="reviewBody"]/text()').extract()
            #print "\n",item['user_review']
            items.append(item)

        return items
