# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GdfjItem(scrapy.Item):
    # define the fields for your item here like:
    '''
    定义需要爬取数据的具体项
    '''
    url = scrapy.Field() #获取当前url
    title= scrapy.Field()#获取标题
    city=scrapy.Field()#获取省级下一级城市名字
    region=scrapy.Field()#获取所在的区域
    district_name=scrapy.Field()#获取所在的街道
    house_desc=scrapy.Field()#获取房子的简介
    house_infor=scrapy.Field()#获取房子的信息
    contact=scrapy.Field()#获取获取联系人
    phone_number=scrapy.Field()#获取联系方式
    update_time=scrapy.Field()#获取更新时间
    
