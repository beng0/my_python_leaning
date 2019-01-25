#coding=utf-8

import requests

def login_():
    url = "https://www.zhihu.com/question/309999495"
    header = {}
    header['accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    header['accept-language'] = "zh-CN,zh;q=0.9"
    header['user-agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    
    r = requests.get(url,headers=header)
    print r.status_code
    print r.content