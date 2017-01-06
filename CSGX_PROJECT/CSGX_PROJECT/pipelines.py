# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
class CsgxProjectPipeline(object):
    def process_item(self, item, spider):
        print item['url']
        #数据库的配置信息
        conn=MySQLdb.connect(
                    host='127.0.0.1',#主机ip
                    port=3306,#端口
                    user='root',#用户名
                    passwd='123456',#密码
                    db='csgx_project',#数据库名字
                    charset='utf8'
                    )
        cursor=conn.cursor()#get the cursor
        '''
        item['title']不能是列表形式，一定要是string类型
        '''
        cursor.execute( "INSERT INTO csgx_project_info (url,title,refer_price,address,developers,area_to_be_demolished,area_be_demolished,area,volume_ratio,stage,transfer_mode,project_properties,identity_of_assignee,project_desc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (item['url'],item['title'],item['refer_price'],item['address'],
                         item['developers'],item['area_to_be_demolished'],item['area_be_demolished'],
                         item['area'],item['volume_ratio'],item['stage'],item['transfer_mode'],item['project_properties'],
                         item['identity_of_assignee'],item['project_desc']))
        conn.commit()    
        cursor.close()
        conn.close()
        return item