'''
Created on 2016.7.21

@author: hadoop
'''
from fangjia.wuyuhang.spider.get_first_url import get_first_url
from fangjia.wuyuhang.scheduler.scheduler import scheduler

if __name__ == '__main__':
    #
    headers = {
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          r'Chrome/51.0.2704.63 Safari/537.36',
            'Referer': r'http://bj.fangjia.com/ershoufang',
            'Host': r'bj.fangjia.com',
            'Connection': 'keep-alive'
        }
    url=r'http://yanan.fangjia.com/ershoufang/--e-98#pagelist'
    scheduler()