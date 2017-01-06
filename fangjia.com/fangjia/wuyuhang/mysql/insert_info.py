'''
Created on 2016.7.23

@author: hadoop
'''
import MySQLdb
from fangjia.wuyuhang.spider import get_page
import urllib2
from fangjia.wuyuhang.scheduler.global_var import global_var
                                                 
def inser_infor(city,region,district_name,title,house_desc,house_infor,contact,phone_number,update_time,img_url,last_url):
    
    #build the connection
    conn=MySQLdb.connect(
                    host='127.0.0.1',#hostname
                    port=3306,#portname
                    user='root',#username
                    passwd='',#password
                    db='spider',#database_name
                    charset='utf8'
                    )
    cursor=conn.cursor()#get the cursor
    local_url=last_url
    try:
        if img_url:
            for item in img_url:
                fp=open('img_url.txt','a')
                fp.write(item)
                fp.write('\n')
                fp.close()         
            img=urllib2.urlopen(img_url[0]).read() 
        else:
            img = ""
        try:
            cursor.execute( "INSERT INTO info (local_url,city,region,district_name,title,house_desc,house_infor,contact,phone_number,update_time,img) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(local_url,city,region,district_name,title,house_desc,house_infor,contact,phone_number,update_time,MySQLdb.Binary(img)))
            conn.commit()    
            cursor.close()
            conn.close()
        except Exception,e:
            print e
            
        
    except Exception,e:
        print e


        