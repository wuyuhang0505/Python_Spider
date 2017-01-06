# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from lxml import etree
from scrapy import Request
from CSGX_PROJECT.items import CsgxProjectItem

class ScrapyInfo(Spider):
    name = "cgsx1"
    urls=[]
    '''
    读文件
    '''

    fb=open("first_url.txt","r")
    for url in fb.readlines():
        urls.append(url.replace('\n',''))    
    fb.close() 

    start_urls = urls #给入口url赋值
    
    cookies = {}       #定义cookie

    # 发送给服务器的http头信息，有的网站需要伪装出浏览器头进行爬取，有的则不需要
    headers = {
         # 'Connection': 'keep - alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }

    # 对请求的返回进行处理的配置
    meta = {
        'dont_redirect': True,  # 禁止网页重定向
        'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    }
    
    urls=[] #存储所有url
    '''
    获取每一页的url列表
    '''
    def get_page_urllist(self,req):
        link_=req.xpath("//div[@class='txt']/a/@href")
        link=['http://CSGX.szhome.com'+i for i in link_]
        return link
  
    def parse(self, response):
        req=etree.HTML(response.body.decode('utf-8'))
        search_list=self.get_page_urllist(req)
        #print search_list[0]
        for url in search_list:
            yield Request(url,callback=self.get_info_parse, headers=self.headers,
                        cookies=self.cookies, meta=self.meta)#获取下一页url面再次调用第二次迭代的函数second_parse 
    
    '''
    获取所有的信息
    '''    
    def get_info_parse(self,response):
        req=etree.HTML(response.body.decode('utf-8'))
        item=CsgxProjectItem() #定义item对象
        item['url']=response.url #获取当前url
        item['title']=self.get_title(req)[0]#获取城市
        refer_price_and_stage=self.get_refer_price_and_stage(req)#获取参考价格和项目状态
        item['refer_price']=refer_price_and_stage[0]#得到参考价格
        print item['refer_price']#打印参考价格
        item['stage']=refer_price_and_stage[1]#得到项目状态
        print item['stage']
        item['project_desc']=self.get_project_desc(req)#获取项目详情
        rest_info=self.get_rest_info(req)#获取剩余的信息
        if len(rest_info)==9:
            item['address']=rest_info[0]#地址
            item['developers']=rest_info[1]#开发商
            item['area_to_be_demolished']=rest_info[2]#待拆迁建筑面积
            item['area_be_demolished']=rest_info[3]#已批准拆迁建筑面积
            item['area']=rest_info[4]#面积
            item['volume_ratio']=rest_info[5]#容积率
            item['transfer_mode']=rest_info[6]#转让方式
            item['project_properties']=rest_info[7]#项目性质
            item['identity_of_assignee']=rest_info[8]#转让人身份
            yield item #返回item对象给pipeline（管道）处理
        else:
            item['address']=''#地址
            item['developers']=rest_info[0]#开发商
            item['area_to_be_demolished']=rest_info[1]#待拆迁建筑面积
            item['area_be_demolished']=rest_info[2]#已批准拆迁建筑面积
            item['area']=rest_info[3]#面积
            item['volume_ratio']=rest_info[4]#容积率
            item['transfer_mode']=rest_info[5]#转让方式
            item['project_properties']=rest_info[6]#项目性质
            item['identity_of_assignee']=rest_info[7]#转让人身份
            yield item #返回item对象给pipeline（管道）处理
    
    '''
    获取标题
    '''    
    def get_title(self,req):
            title_=req.xpath("//div[@class='detail-head']/h1/text()")
            title=[i.strip() for i in title_]
            return title 
    '''
    获取参考价格和项目状态
    '''    
    def get_refer_price_and_stage(self,req):
            refer_price_and_stage_=req.xpath("//div[@class='pd20 f14 fix']/p/span/text()")
            mid=[i.strip() for i in refer_price_and_stage_]
            refer_price_and_stage=[]
            for item in mid:
                if item!='':
                    refer_price_and_stage.append(item)
            return refer_price_and_stage
     
    '''
    获取项目详情 
     '''           
    def get_project_desc(self,req):
            project_desc_=req.xpath("//div[@class='pd20 f14 fix']/text()")
            mid=[i.strip() for i in project_desc_]
            project_desc=''
            for item in mid:
                if item!='':
                    project_desc=project_desc+item
            return project_desc
    
    '''
    获取剩余的信息
    '''    
    def get_rest_info(self,req):
            rest_info_=req.xpath("//div[@class='pd20 f14 fix']/p/text()")
            mid=[i.strip() for i in rest_info_]
            rest_info=[]
            for item in mid:
                if item!='':
                    rest_info.append(item)
            return rest_info
            
        
        
        
              