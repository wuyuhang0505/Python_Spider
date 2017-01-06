import urllib2
from fangjia.wuyuhang.scheduler.global_var import global_var
def get_page(url):
    
    req = urllib2.Request(url)
    response = urllib2.urlopen(req).read()
    #page = response.decode('utf-8')
    global_var.page = response
