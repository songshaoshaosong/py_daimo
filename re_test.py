#__author__=''
# -*- coding:utf-8 -*-
import re
import requests

def getPage():
    # 获取页面信息
    # 构造页面请求
    url = 'http://www.dy2018.com/html/gndy/dyzz/index.html'
    page = 'http://www.dy2018.com'
    html_url=[]
    response = requests.get(url)
    #print response.status_code,response.headers['content-type'],response.encoding,response.content
    #response.encoding='GB2312'
    dytext = response.content
    pattern=re.compile(r'<b>.*?<a.*?href="(.*?)".*?</b>',re.S)
    result = re.findall(pattern, dytext)
    for m in result:
        html_url.append(page+m)
        #print html_url
    return html_url
def getfame():
    for u in getPage():
        res=requests.get(u)
        ftext=res.content
        pat=re.compile(r'<p>◎片.*?名(.*?)</p>.*?迅雷下载地址.*?style="WORD-WRAP:.*?><a.*?href="(.*?)">ftp:.*?',re.S)
        resu=re.findall(pat,ftext)
        for i in resu:
            print i[0],i[1]

def main():
    getfame()
main()