#from scrapy.spiders import Spider
from scrapy.selector import Selector
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from apartmentguide_ratings_crawler.items import ApartmentguideRatingsCrawlerItem


class ApartmentguideSpider(CrawlSpider):
    name = "apartguiderat"
    allowed_domains = ["apartmentguide.com"]
    start_urls = [
        'http://www.apartmentguide.com/apartments/Alabama/Madison/Grand-Reserve-At-Madison/28587',
    ]

    rules = ( 
        Rule(LinkExtractor(restrict_xpaths='//details_reviews[@class="review_box"]'), callback='parse_pages'),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="page"]')),)


    # def parse_start_url(self,response):

    #     return self.parse_pages(response)
        # items = []
        # users = response.xpath('//div[@class="review_box"]')
        # #print "\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",users
        # for user in users:

        #     item = ApartmentguideRatingsCrawlerItem()
                    
        #     item['username']    = user.xpath('//div[@class="review_box"]/div[@class="review_rating"]/text()').extract()
        #     item['user_rating'] =user.xpath('//div[@class="review_box"]/div[@class="review_rating"]/span[@itemprop="ratingValue"]/text()').extract()
        #     #print "\n",item['user_rating']'''
        #     item['review_date'] =user.xpath('//div[@class="review_box"]/p[@class="review_date"]/text()').extract()
        #     #print "\nreview_date: ",item['review_date']
        #     item['user_review'] =user.xpath('//div[@class="review_box"]/p[@itemprop="reviewBody"]/text()').extract()
        #     #print "\n",item['user_review']
        #     items.append(item)

        # return items

   
    def parse_pages(self, response):

        
        items = []
        # print "\ntttttttttttttttttttttttttResponse>>>",type(response)
        # print "\nrrrrrrrrrrrrrrrrrrrRRRRRRResponse>>>",response

        # pages = len(response.xpath('//div[@class="ld_tab_content"]/div[@id="details_ratings_reviews"]/div[@id="details_reviews"]/div[@id="reviews_container"]/div[@class="pagination"]/ol/li'))

        users = response.xpath('//div[@class="ld_tab_content"]/div[@id="details_ratings_reviews"]/div[@id="details_reviews"]/div[@id="reviews_container"]/div[@itemprop="review"]')
        # # for page  in range (1,pages):
        # #     url=
        # #     yield scrapy.Request(url, callback=self.parse_page_contents)

        for user in users:

            item = ApartmentguideRatingsCrawlerItem()
            
            item['username']    = user.xpath('a[@class="author"]/text()').extract()
            item['user_rating'] =user.xpath('div[@itemprop="reviewRating"]/div[@class="result-rating one "]/meta/@content').extract()
            #print "\n",item['user_rating']
            item['review_date'] =user.xpath('p[@class="review_date"]/text()').extract()
            #print "\nreview_date: ",item['review_date']
            item['user_review'] =user.xpath('p[@class="review-response"]/text()').extract()
            #print "\n",item['user_review']
            items.append(item)

        # users = response.xpath('//details_reviews[@class="review_box"]')
        # #print "\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",users
        # for user in users:

        #     item = ApartmentguideRatingsCrawlerItem()
                    
        #     item['username']    = user.xpath('div[@class="review_rating"]/text()').extract()
        #     item['user_rating'] =user.xpath('div[@class="review_rating"]/span[@itemprop="ratingValue"]/text()').extract()
        #     #print "\n",item['user_rating']'''
        #     item['review_date'] =user.xpath('p[@class="review_date"]/text()').extract()
        #     #print "\nreview_date: ",item['review_date']
        #     item['user_review'] =user.xpath('p[@itemprop="reviewBody"]/text()').extract()
        #     #print "\n",item['user_review']
        #     items.append(item)

        return items
