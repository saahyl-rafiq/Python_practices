from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.selector import HtmlXPathSelector
from besthospitals.items import BesthospitalsItem

class Hospital_spider(CrawlSpider):
    name = "rank"
    allowed_domains = ["health.usnews.com"]
    start_urls = ['http://health.usnews.com/best-hospitals/rankings/']

    rules = (Rule(SgmlLinkExtractor(allow=(r'/best-hospitals/rankings/.+',)), callback='parse_items'),
    )

    def parse_items(self,response):
        #hxs = HtmlXPathSelector(response)
        print "\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.",response.url
        #print "\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>.>>>>>>>>>>>>>>>>>>\n\ntype=",hxs.select('//div[@class="unwrap t-close"]/a/text()').extract()
        #titles = hxs.select('//div[@class="unwrap t-close"]')
        titles = response.xpath('//div[@class="sep-generous button-hover_container"]')
        items = []
        for title in titles:
            item = BesthospitalsItem()
            
            #item ["title"] = title.select("h3/a/text()").extract()
            item ["title"] = title.xpath('div[@class="clearfix"]/div[@class="unwrap t-close"]/h3/a/text()').extract()
            print "\n TITLE=",item ["title"] 
            item ["address"] = title.select('div[@class="clearfix"]/div[@class="unwrap t-close"]/p/text()').extract()
            print "\n Address=", item["address"]
            item ["hos_type"] = title.xpath('div[@class="clearfix"]/div[@class="t-slack"]/p[2]/text()').extract()
            print "\nType=", item["hos_type"]


            items.append(item)
        return(items)