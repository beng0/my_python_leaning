#coding=utf-8

import requests
token = ''

def login_(account,pwd,vc=''):
    url = "https://test.umaicloud.com/api/user/login"
    
    data = {"account":account,"pwd":pwd,"verify_code":vc,"uuid":"cb3df828-ef37-47a5-8bfe-79b89acec373"}
    r = requests.post(url,data)
#     print r.status_code
    content = eval(r.content)
    if content.has_key("token"):
        global token
        token = content["token"]
    return content["code"],content["msg"],content.has_key("token")
login_("13418685311", "12345678a")

def ware_house(name):
    header = {}
    header["Auth-Token"] = token
    url = "https://test.umaicloud.com/api/ware_house/add"
    data = {"name":name,"contact":"lilei","telephone":13400012000,"address":"shenzhen"}
    r = requests.post(url,data,headers=header)
    print r.content
    content = eval(r.content)
    return content['code'],content['msg'],content.has_key("id")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    