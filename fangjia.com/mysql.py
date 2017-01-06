import MySQLdb
from bs4 import BeautifulSoup as BS
import re
from fangjia.wuyuhang.spider import get_page
                                                 
url=r'http://bj.fangjia.com/ershoufang/--r-%E4%B8%B0%E5%8F%B0%7Cb-%E4%B8%B0%E5%8F%B0%E4%BD%93%E8%82%B2%E9%A6%86'
#获取界面
page=geget_pagerl)
#将page变成BS对象处理
soup = BS(page, 'lxml')  
title_list = soup.select('a[class="h_name"]')
address_list = soup.select('span[class="address]')
attr_list = soup.select('span[class="attribute"]')
price_list = soup.find_all(attrs={"class": "xq_aprice xq_esf_width"})
#建立连接
conn=MySQLdb.connect(
                    host='127.0.0.1',#主机名
                    port=3306,#端口号
                    user='root',#用户名
                    passwd='',#密码
                    db='spider',#数据库
                    charset='utf8'
                    )
cursor=conn.cursor()#获取游标
#查看列表信息个数
def get_item_num():
    item_num=0
    for num in range(30):
        try:
            if(title_list[num].attrs["title"]):
                item_num=item_num+1
            else:
                break
        except:
            continue
    return item_num
item_num=get_item_num()
area=''
#开始查找
for num in range(item_num):
    print num
    try:
        title = title_list[num].attrs["title"]
        address = re.sub('\n\n', '\n', address_list[num].get_text())
        area =re.search('\d\d+[^0-9][^0-9][^0-9]', attr_list[num].get_text()).group(0)
        layout = re.search('\d[^0-9]\d.', attr_list[num].get_text()).group(0)
        floor = re.search('\d/\d', attr_list[num].get_text()).group(0)
        price = re.search('\d+[\u4E00-\u9FA5][^0-9]', price_list[num].get_text()).group(0)
        unit_price = re.search('\d+[^0-9]/[^0-9]', price_list[num].get_text()).group(0)
        #定义SQL语句
        sql_insert="insert into house_price(title,addr,area,layout,floor,price,unit_price) values('%s','%s','%s','%s','%s','%s','%s')"%(title,address,area,layout,floor,price,unit_price)
        #插入表
        cursor.execute(sql_insert)
        #提交信息
        conn.commit()    
    except:        
        continue  
#关闭游标  
cursor.close()
#关闭连接
conn.close()    