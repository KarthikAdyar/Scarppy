# -*- coding: utf-8 -*-
import scrapy
from ..items import GoogleProjectItem

class GoogleSpyderSpider(scrapy.Spider):
    name = 'google_spyder'

    start_urls = ['http://cloud.google.com/datastore/docs/']

    def parse(self, response):
        #items = GoogleProjectItem()

       # allGoogleItems1 = response.xpath("//ul[@class='devsite-nav-list devsite-nav-expandable']/li[@class = 'devsite-nav-item devsite-nav-item-heading']/span[@class='devsite-nav-title devsite-nav-title-no-path']")
        allgoogleitems2 = response.xpath("//li[@class ='devsite-nav-item']/a[@class = 'devsite-nav-title gc-analytics-event']")
       # for item in allGoogleItems1:
        #    title = item.css('span::text').extract()
         #   yield {'item': title}
        for item in allgoogleitems2:
            subtitle = item.css('span::text').extract()
            yield {'item': subtitle}

