'''
Created on 2016.7.21

@author: hadoop
'''
from fangjia.wuyuhang.spider.get_first_url import get_first_url
from fangjia.wuyuhang.spider.stack import stack
from fangjia.wuyuhang.spider.get_next_pagelist import get_next_pagelist
import re
from fangjia.wuyuhang.scheduler.global_var import global_var
from fangjia.wuyuhang.spider.get_page import get_page
from fangjia.wuyuhang.spider.get_last_pagelist import get_last_pagelist
from bs4 import BeautifulSoup
from fangjia.wuyuhang.spider.get_all_info import get_all_info
from fangjia.wuyuhang.mysql.insert_info import inser_infor

def scheduler():
    #get the fist_url
    url=r'http://maoming.fangjia.com/ershoufang/'
    first_url=get_first_url(url)
    #define a temporary stack and save first_url
    
    for item in first_url:
        fp=open('first_url.txt','w')
        for i in first_url:
            fp.write(first_url[i])
            fp.write('\n')
        fp.close()
       
######################################################
    '''
    long_url_tail=r'/ershoufang/--e-1#pagelist'
    ff=open('first_url.txt','r')
    s_tmp=ff.readlines()
    ff.close()          
    for url in s_tmp:
        if (len(url)==0):
            print 'the whole pagelists are loaded'
            break 
        else:
            shirt_url_head=re.search(r'http:\D+\.com',url).group(0)
            whole_url=shirt_url_head+long_url_tail
            try:
                long_url_tail=r'/ershoufang/--e-1#pagelist' 
                shirt_url_head=re.search(r'http:\D+\.com',url).group(0)
                whole_url=shirt_url_head+long_url_tail
                long_url_head=re.search(r'http:\D+\e-',whole_url).group(0)
                shirt_url_tail=re.search(r'#\D+',whole_url).group(0)
                
                i=1
                while(i):
                    whole_url=long_url_head+str(i)+shirt_url_tail
                    i=i+1
                    get_page(whole_url)
                    if(len(get_next_pagelist())==0):
                        last_pagelist=get_last_pagelist()
                        for item in last_pagelist:
                            fp=open('last_pagelist.txt','a')
                            fp1=open('img_url.txt','a')
                            fp.write(last_pagelist[item])
                            fp.write('\n')
                            fp1.write(last_pagelist[item])
                            fp1.write('\n')
                            last_url=last_pagelist[item]
                            get_page(last_url)
                            g_var=global_var()
                            g_var.last_url=last_url
                            page=g_var.page
                            soup = BeautifulSoup(page,"lxml")
                            try:
                                city=get_all_info(soup).get_city()
                                region=get_all_info(soup).get_region()
                                district_name=get_all_info(soup).get_district_name()
                                title= get_all_info(soup).get_title()
                                house_desc=get_all_info(soup).get_house_desc()
                                house_infor=get_all_info(soup).get_house_infor()
                                contact=get_all_info(soup).get_contact()
                                phone_number=get_all_info(soup).get_phone_number()
                                update_time=get_all_info(soup).update_time()
                                img_url=get_all_info(soup).get_img_url()                              
                                inser_infor(city,region,district_name,title,house_desc,house_infor,contact,phone_number,update_time,img_url,last_url)
                            except Exception,e:
                                print "scheduler.py line:80"
                                print e
                            fp.close()
                            fp1.close()
                        break
                    else:
                        last_pagelist=get_last_pagelist()
                        for item in last_pagelist:
                            # print last_pagelist[item]
                            fp=open('last_pagelist.txt','a')
                            fp.write(last_pagelist[item])
                            fp.write('\n')
                            fp.close()
                            fp1=open('img_url.txt','a')
                            fp1.write(last_pagelist[item])
                            fp1.write('\n')
                            fp1.close() 
                            last_url=last_pagelist[item]
                            get_page(last_url)
                            g_var=global_var()
                            g_var.last_url=last_url
                            page=g_var.page
                            soup = BeautifulSoup(page,"lxml")
                            try:
                                city=get_all_info(soup).get_city()
                                region=get_all_info(soup).get_region()
                                district_name=get_all_info(soup).get_district_name()
                                title= get_all_info(soup).get_title()
                                house_desc=get_all_info(soup).get_house_desc()
                                house_infor=get_all_info(soup).get_house_infor()
                                contact=get_all_info(soup).get_contact()
                                phone_number=get_all_info(soup).get_phone_number()
                                update_time=get_all_info(soup).update_time()
                                img_url=get_all_info(soup).get_img_url()                              
                                inser_infor(city,region,district_name,title,house_desc,house_infor,contact,phone_number,update_time,img_url,last_url)
                            except Exception,e:
                                print "scheduler.py line:110"
                                print e
                                continue       
            except Exception,e:
                continue
'''              
   
                 
            
            
        
        
        
        
        
        
           
    