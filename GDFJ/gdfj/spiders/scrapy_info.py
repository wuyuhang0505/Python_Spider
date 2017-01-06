# -*- coding: utf-8 -*-
'''
Created on 2016��12��9��

@author: YH
'''

from scrapy.spiders import Spider
from gdfj.items import GdfjItem  # �˴����������pyCharm��ԭ��
from bs4 import BeautifulSoup
from scrapy import Request
import re
from scrapy.item import Item
from gdfj.spiders.get_all_info import get_all_info

class ScrapyInfo(Spider):
    '''
           前置参数设定
    '''
    name = "gdfj"      #定义唯一爬虫命名
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
    
    urls=[] #存储所有广东的
    '''
           读文件
    ''' 
    fb=open("first_url.txt","r")
    for url in fb.readlines():
        urls.append(url.replace('\n',''))    
    fb.close()
    start_urls=urls #初始url，也就是入口urls
    
    
    '''
          获第一页的url
    '''
    def get_fisrt_page_url(self,url):#将获取的url加上后缀
        url_head=re.search(r'http:\D+\.com',url).group(0) #url的头部
        url_tail=r'/ershoufang/--e-1#pagelist' #url的尾部
        whole_url=url_head+url_tail #完整的url
        return whole_url #返回完整的url
    
    '''
    获取下一页的url
    '''
    def get_next_url(self,page):
       
        def has_attr(tag):#提取第二页的url标签
            return tag.has_attr('href') and tag.has_attr('title')and tag.has_attr('rel')
        
        soup=BeautifulSoup(page,'lxml')#把response.body实例化成BS形态        
        search_list=soup.select('a[class="next"]') #获取class=next标签的元素

        next_url_tail=''
        if (search_list!=[]):
            soup = BeautifulSoup(str(search_list[0]), 'lxml') #
            #get the next pagelist
            next_url_tail = soup.a.attrs['href'] #返回key
            #print next_url_tail
        else:
            return next_url_tail
        return next_url_tail
    '''
    第一次进入的函数，也即是主调函数
    '''
    def parse(self, response):
        #print response.body
        fisrt_page_url = self.get_fisrt_page_url(response.url) #第一次迭代的url
        
        soup=BeautifulSoup(response.body,'lxml') #将response.body BS实例化
        search_list=self.get_page_info_url_list(soup)#获取此页面所有列表的最后一级url
        #这里应该是获取第一个页面的所有信息
        for url in search_list:
            yield Request(search_list[url],callback=self.get_info_parse, headers=self.headers,
                        cookies=self.cookies, meta=self.meta)#获取下一页url面再次调用第二次迭代的函数second_parse 
        next_url_tail=self.get_next_url(response.body) #获取第二页的url头部
        if(next_url_tail!=None):
            next_url_head=re.search(r'http:\D+\.com',fisrt_page_url).group(0) #url的头部
            whole_url=next_url_head+next_url_tail #完整的url
            print whole_url
            #这里应该是获取第二个页面的所有信息
            yield Request(whole_url,callback=self.second_parse, headers=self.headers,
                        cookies=self.cookies, meta=self.meta) #获取下一页url面再次调用第二次迭代的函数second_parse   
        #print fisrt_page_url
    '''
    再次定义回调函数，与parse相互迭代
    '''   
    def second_parse(self, response):#这是进入具体页面爬取所需信息的
        
        next_page_url = self.get_fisrt_page_url(response.url)#下次迭代的url
        soup=BeautifulSoup(response.body,'lxml') #将response.body BS实例化
        search_list=self.get_page_info_url_list(soup)#获取此页面所有列表的最后一级url
        
        #此循环将获取一个页面所有信息
        for url in search_list:
            yield Request(search_list[url],callback=self.get_info_parse, headers=self.headers,
                        cookies=self.cookies, meta=self.meta)#获取下一页url面再次调用第二次迭代的函数second_parse  
        
        #判断有没有下一页
        next_url_tail=self.get_next_url(response.body) #获取下一页的url头部
        if(next_url_tail!=None):
            next_url_head=re.search(r'http:\D+\.com',next_page_url).group(0) #url的头部
            whole_url=next_url_head+next_url_tail #完整的url
            yield Request(whole_url,callback=self.second_parse, headers=self.headers,
                        cookies=self.cookies, meta=self.meta)#获取下一页url面再次调用第二次迭代的函数second_parse  
    ''' 
            获取此页面所有列表的最后一级url  
    '''  
    def get_page_info_url_list(self,soup):
        
        def has_class_but_no_id(tag):
            return tag.has_attr('class') and tag.has_attr('title') and tag.has_attr('target')#获取链接规则
        
        search_dict={} #定义存储字典
        #开始寻找
        search_list=soup.find_all(has_class_but_no_id)#得出url列表
        #循环将search_list分解成字典
        for i in range(len(search_list)):
            #将search_list[i]变成BS形式
            soup = BeautifulSoup(str(search_list[i]), 'lxml')
            #获取key
            key = soup.select('a')[0].get_text()
            #获取value
            value = soup.a.attrs['href']
            search_dict[key] = value#赋值
        return search_dict#返回字典    

        '''
                        获取一个网页的全部信息
        '''
    def get_info_parse(self,response):
        soup = BeautifulSoup(response.body,"lxml",from_encoding='utf-8')
        item=GdfjItem()
        item['url']=response.url
        item['city']=get_all_info(soup).get_city()#获取城市
        item['title']= get_all_info(soup).get_title()#获取标题
        item['region']=get_all_info(soup).get_region()#获取区域
        item['district_name']=get_all_info(soup).get_district_name()#获取街道
        item['house_desc']=get_all_info(soup).get_house_desc()#获取房子简介
        item['house_infor']=get_all_info(soup).get_house_infor()#获取房子信息
        item['contact']=get_all_info(soup).get_contact()#获取联系人
        item['phone_number']=get_all_info(soup).get_phone_number()#获取联系人电话
        item['update_time']=get_all_info(soup).update_time()#获取更新时间
        yield item
