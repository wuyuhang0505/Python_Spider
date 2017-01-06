'''
Created on 2016.7.21

@author: hadoop
'''
import urllib2
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from fangjia.wuyuhang.spider.get_page import get_page
from fangjia.wuyuhang.scheduler.global_var import global_var
def get_first_url(url):
    #get the page information
    get_page(url)
    g_var=global_var
    page=g_var.page
    #change page to a soup object
    soup = BeautifulSoup(page,"lxml")
    #'has_class_but_no_id()' is a method that can filter a tap contains 'name' and 'href' attribute
    def has_class_but_no_id(tag):
        return tag.has_attr('name') and tag.has_attr('href')
    #define 'count' to count the number of url
    count=0
    #'search_dict'is a dict saves key and value of url 
    search_dict={}
    #begin to find
    search_list=soup.find_all(has_class_but_no_id)
    #for loop is to get key and value and put them into search_dict
    for i in range(len(search_list)):
        #change search_list into soup object again
        soup = BeautifulSoup(str(search_list[i]), 'lxml')
        #get key
        key = soup.select('a')[0].get_text()
        count=count+1
        #get value 
        value = soup.a.attrs['href']
        #get search_dict       
        search_dict[key] = value
    return search_dict