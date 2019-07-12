# -*- coding: utf-8 -*-
import scrapy


class ScikitlearnSpySpider(scrapy.Spider):
    name = 'scikitlearn_spy'
    allowed_domains = ['https://scikit-learn.org/stable/modules/classes.html']
    start_urls = ['http://scikit-learn.org/stable/modules/classes.html/']

    def parse(self, response):
        pass
