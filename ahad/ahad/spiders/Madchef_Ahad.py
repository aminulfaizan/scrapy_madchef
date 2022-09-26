# -*- coding: utf-8 -*-
"""

@author: bulbul

menu title 

main item name = '//div[@class="menu"]//div[@class="menu-category-title"]//span//text()'
sub_item_title = '//div[@class="menu-item-title"]//text()'
price = '//div[@class="menu-item-price"]//span//strong//text()'
descrption = '//div[@class="menu-item-description"]//text()'
loop = '//div[@class="menu"]//div[@class="menu-category-title"]'


 item_name=response.xpath('//div[@class="menu-item-title"]/text()').get()
 item_price = response.xpath('//div[@class="menu-item-price"]//span//strong//text()').get()
 item_description=response.xpath('//div[@class="menu-item-description"]//text()').get()
 return {
         'item_name':item_name  ,                           
        # 'sub_item_name': menu.xpath('//div[@class="menu-item-title"]//text()').get(),
         'price':item_price ,
         'descrition': item_description
     }
//div[@class="menumodal-title"]//text()
class="menumodal-category"
class="menumodal-description"


class="branch-address"
//div[@class="branch "]//div[@class="branch-address"]
"""

import scrapy


class MadchefAhad(scrapy.Spider):
    name = 'mad_ahad'
    allowed_domains = ['www.madchef.com.bd']
    start_urls = ['https://madchef.com.bd/menu']

    def parse(self, response):
        for menu in response.xpath('//div[@class="main main-menu"]//div[@class="menumodal modal"]'):
            yield {
                'item_name': menu.xpath('normalize-space(.//div[@class="menumodal-title"]//text())').extract_first(),                                       
                'price': menu.xpath('.//div[@class="menumodal-price"]//span//strong//text()').extract_first(),
                'description': menu.xpath('normalize-space(.//div[@class="menumodal-description"]//text())').extract_first(),
                'category' : menu.xpath('.//div[@class="menumodal-category"]//a/text()').extract_first()
            }
            

    """  next_page = response.xpath(
            "//ul[@class='pagination']/li[position() = last()]/a/@href").get()
                                                             
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)"""