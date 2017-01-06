from bs4 import BeautifulSoup
from fangjia.wuyuhang.scheduler.global_var import global_var
##'get_next_pagelist()' is a fuction that can get pagelist like /ershoufang/--e-2#pagelist
def get_next_pagelist():
    #'has_attr() is a fuction that can filter a tap contains 'name' and 'href' attribute
    def has_attr(tag):
        return tag.has_attr('href') and tag.has_attr('title')and tag.has_attr('rel')
    #define global variable object
    g_var=global_var
    #get the page
    page=g_var.page
    #make a soup object
    soup=BeautifulSoup(page,'lxml')
    #fine the information contains next pagelist
    search_list=soup.select('a[class="next"]')
    #make search_list a soup object again
    key=''
    if (search_list!=[]):
        soup = BeautifulSoup(str(search_list[0]), 'lxml')
        #get the next pagelist
        key = soup.a.attrs['href']
    else:
        return key
    return key