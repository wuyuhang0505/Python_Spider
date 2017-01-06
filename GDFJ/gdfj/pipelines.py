# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
class GdfjPipeline(object):
    def process_item(self, item, spider):
        print item['url']
        #数据库的配置信息
        conn=MySQLdb.connect(
                    host='127.0.0.1',#主机ip
                    port=3306,#端口
                    user='root',#用户名
                    passwd='123456',#密码
                    db='gdfj',#数据库名字
                    charset='utf8'
                    )
        cursor=conn.cursor()#get the cursor
        cursor.execute( "INSERT INTO fjw (url,city,title,region,district_name,house_desc,house_infor,contact,phone_number,update_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (item['url'],item['city'],item['title'],item['region'],item['district_name'],item['house_desc'],
                         item['house_infor'],item['contact'],item['phone_number'],item['update_time']))
        conn.commit()    
        cursor.close()
        conn.close()
        return item
    '''
        item['url']
        item['city']
        item['title']
        item['region']
        item['district_name']
        item['house_desc']
        item['house_infor']
        item['contact']
        item['phone_number']
        item['update_time']
    '''