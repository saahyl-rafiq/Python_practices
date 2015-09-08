# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class RentdotcomRatingsCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    property_name  = scrapy.Field()
    username       = scrapy.Field()
    user_rating    = scrapy.Field()
    review_date    = scrapy.Field()
    user_review    = scrapy.Field()
