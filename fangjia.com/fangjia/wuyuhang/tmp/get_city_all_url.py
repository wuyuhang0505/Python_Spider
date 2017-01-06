import re
from fangjia.wuyuhang.spider.get_next_pagelist import get_next_pagelist
from fangjia.wuyuhang.spider.get_page import get_page
from fangjia.wuyuhang.scheduler.global_var import global_var
from fangjia.wuyuhang.spider.stack import stack

def get_city_all_url(whole_url):
    long_url_head=re.search(r'http:\D+\e-',whole_url).group(0)
    global_var.long_url_head=long_url_head
    shirt_url_tail=re.search(r'#\D+',whole_url).group(0)
    global_var.shirt_url_tail=shirt_url_tail
    g_var=global_var
    i=1
    while(i):
        whole_url=long_url_head+str(i)+shirt_url_tail
        get_page(whole_url)
        if(get_next_pagelist()==''):
            g_var.city_url_s.push(whole_url)
            break
        else:
            g_var.city_url_s.push(whole_url)
            i=i+1
