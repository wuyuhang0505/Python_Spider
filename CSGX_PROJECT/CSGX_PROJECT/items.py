# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsgxProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field() #当前url
    title= scrapy.Field()#标题
    refer_price=scrapy.Field()#参考价格
    address=scrapy.Field()#地址
    developers=scrapy.Field()#开发商
    area_to_be_demolished=scrapy.Field()#待拆迁建筑面积
    area_be_demolished=scrapy.Field()#已批准拆迁建筑面积
    area=scrapy.Field()#面积
    volume_ratio=scrapy.Field()#容积率
    stage=scrapy.Field()#所属阶段
    transfer_mode=scrapy.Field()#转让方式
    project_properties=scrapy.Field()#项目性质
    identity_of_assignee=scrapy.Field()#转让人身份
    project_desc=scrapy.Field()#项目详情
    img=scrapy.Field()#图片url
