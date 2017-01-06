import re
from fangjia.wuyuhang.scheduler.global_var import global_var
from fangjia.wuyuhang.spider.get_page import get_page
from fangjia.wuyuhang.spider.get_last_pagelist import get_last_pagelist
from bs4 import BeautifulSoup
from fangjia.wuyuhang.spider.get_all_info import get_all_info
from fangjia.wuyuhang.spider.get_next_pagelist import get_next_pagelist
url=r'http://nc.fangjia.com/ershoufang-xinxi-57d2ed99e4b0d0c6df00a3bb'

get_page(url)
g_var=global_var()
value=[]
page=g_var.page
soup = BeautifulSoup(page,"lxml")
search_list=soup.find_all("div", class_="fr")
soup = BeautifulSoup(str(search_list[0]), 'lxml')
#soup='2016-09-09 gengxing'
pattern = re.compile(r'\d+[...]\d+')
soup=soup.select('div')[0].get_text()
print re.findall(pattern, soup) 
'''
def has_class_but_no_id(tag):
    return tag.has_attr('name') and tag.has_attr('data-original')
search_list=soup.find_all(has_class_but_no_id)
for i in range(len(search_list)):
    soup = BeautifulSoup(str(search_list[i]), 'lxml')
    v= soup.img.attrs['data-original']
    value.append(v)
    print v
for item in value:
        fp=open('img_url1.txt','a')
        fp.write(item)
        fp.write('\n')
        fp.close() 

long_url_tail=r'/ershoufang/--e-1#pagelist' 
shirt_url_head=re.search(r'http:\D+\.com',url).group(0)
whole_url=shirt_url_head+long_url_tail
print whole_url
long_url_head=re.search(r'http:\D+\e-',whole_url).group(0)
shirt_url_tail=re.search(r'#\D+',whole_url).group(0)

i=1
while(i):
    whole_url=long_url_head+str(i)+shirt_url_tail
    i=i+1
    print whole_url
    get_page(whole_url)
    if(len(get_next_pagelist())==0):
        last_pagelist=get_last_pagelist()
        for item in last_pagelist:
            fp=open('last_pagelist2.txt','a')
            for item in last_pagelist:
                fp.write(last_pagelist[item])
                fp.write('\n')
            fp.close()
        break
    else:
        last_pagelist=get_last_pagelist()
        for item in last_pagelist:
            print last_pagelist[item]
            fp=open('last_pagelist2.txt','a')
            fp.write(last_pagelist[item])
            fp.write('\n')
            fp.close()      
'''    
