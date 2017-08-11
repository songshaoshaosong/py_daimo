#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# _*_ Author:Yee
import requests
url='http://www.dy2018.com/i/98220.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
   'Referer': 'http://www.dy2018.com/html/gndy/dyzz/index_2.html',
   'Connection': 'Keep-Alive'}
cookies={'Hm_lvt_a68dc87e09b2a989eec1a0669bfd59eb':'1502420224','Hm_lpvt_a68dc87e09b2a989eec1a0669bfd59eb':'1502433052','91turn_1886':'1'}
cookie=requests.utils.cookiejar_from_dict(cookies)
response=requests.session()
response.get(url,headers=headers,cookies=cookie)
print response.cookies



