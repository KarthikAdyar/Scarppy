# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonProjectItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'

    start_urls = [
        'https://www.amazon.in/s?k=smartphones&ref=nb_sb_noss_2'
    ]

    def parse(self, response):
        items = AmazonProjectItem()


        product_name = response.css('.a-text-normal , #nav-al-title').css('::text').extract()
        product_price = response.css('.a-price-whole').css('::text').extract()
        product_image =response.css('.s-image-fixed-height::attr(src)').extract()


        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_image'] = product_image

        yield items