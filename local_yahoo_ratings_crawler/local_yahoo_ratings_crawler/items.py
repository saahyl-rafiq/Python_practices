# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LocalYahooRatingsCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #entity_title=scrapy.Field()
    #entity_type=scrapy.Field()
    username=scrapy.Field()
    user_rating=scrapy.Field()
    review_date=scrapy.Field()
    user_review=scrapy.Field()
