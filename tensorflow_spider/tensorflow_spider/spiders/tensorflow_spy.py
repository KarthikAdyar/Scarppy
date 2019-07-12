# -*- coding: utf-8 -*-
#Comment from Vikas

import scrapy
from ..items import TensorflowSpiderItem

class TensorflowSpySpider(scrapy.Spider):
    name = 'tensorflow_spy'

    start_urls = ['http://www.tensorflow.org/api_docs']

    def parse(self, response):
        item = TensorflowSpiderItem()

        allTensorflowItems = response.xpath("//ul[@class = 'devsite-nav-list']/li[@class ='devsite-nav-item' ]/a[@class ='devsite-nav-title']/span[@class = 'devsite-nav-text']").css("::text").extract()
        allTensorflowItems1 = response.xpath("//ul[@class = 'devsite-nav-list']/li[@class ='devsite-nav-item' ]/a[@class ='devsite-nav-title']").css("::attr(href)").extract()
        for i in range(0, len(allTensorflowItems1)):
            item['title'] = allTensorflowItems[i]
            if allTensorflowItems1[i][0:4] !='http':
                item['link'] ='https://www.tensorflow.org'+ allTensorflowItems1[i]
            else:
                item['link'] =  allTensorflowItems1[i]
            yield item
        allTensorflowItems = response.xpath("//ul[@class = 'devsite-nav-list']/li[@class ='devsite-nav-item           devsite-nav-external' ]/a[@class ='devsite-nav-title']/span[@class = 'devsite-nav-text']").css("::text").extract()
        allTensorflowItems1 = response.xpath("//ul[@class = 'devsite-nav-list']/li[@class ='devsite-nav-item           devsite-nav-external' ]/a[@class ='devsite-nav-title']").css("::attr(href)").extract()
        for i in range(0, len(allTensorflowItems1)):
            item['title'] = allTensorflowItems[i]
            item['link'] = allTensorflowItems1[i]
            yield item
        '''for item in allTensorflowItems:
            title = item.css('span::text').extract()
            yield [title]'''

