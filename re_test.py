#__author__=''
# -*- coding:utf-8 -*-
import re
import requests
import os
import time
from multiprocessing import Pool

def getPage(url):
    # 获取页面信息
    # 构造页面请求
    #url = 'http://www.dy2018.com/html/gndy/dyzz/index.htm l'
    page = 'http://www.dy2018.com'
    html_url=[]
    headers = {"Connection": "close",'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Referer':'http://www.dy2018.com/'}
    response = requests.get(url,headers=headers,timeout=5)
    print response.cookies.values()
    #response.encoding='GB2312'
    print url
    dytext = response.text
    response.close()
    time.sleep(3)
    pattern=re.compile(r'<b>.*?<a.*?href="(.*?)".*?</b>',re.S)
    result = re.findall(pattern, dytext)
    for m in result:
        html_url.append(page+m)
        #print html_url
    return html_url
def getfame(html_url):
    for u in html_url:
        headers = {"Connection": "close",'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Referer':'http://www.dy2018.com/'}
        res=requests.get(u,headers=headers,timeout=5)
        print res.cookies
        res.encoding='gb2312'
        ftext=res.text
        res.close()
        #ftext.encode('gb2312','ignore')

        pat=re.compile(r'<!--Content Start-->.*?<p>.*?<img src=".*?alt.*?</p>.*?<p(.*?)</p>.*?<!--xunleiDownList Start-->.*?<td style="WORD-WRAP.*?<a href="(.*?)">ftp://',re.S)
        resu=re.findall(pat,ftext)
        for i in resu:
            #print i[0]
            f = open('dygod.txt', 'a+')
            f.write(i[0].encode('gbk','ignore')+'  '+i[1].encode('gbk','ignore')+'\n')
            f.flush()
            f.close()
def geturls():
    urls=[]
    for index in range(1,295):
        if index==1:
            #print '下载第：'+str(index)+'页'
            url = 'http://www.dy2018.com/html/gndy/dyzz/index.html'
            urls.append(url)
        else:
            #print '下载第：' + str(index) + '页'
            #print 'http://www.dy2018.com/html/gndy/dyzz/index_'+str(index)+'.html'
            urls.append('http://www.dy2018.com/html/gndy/dyzz/index_'+str(index)+'.html')
    return urls
def main(url):
    result=getPage(url)
    #print result
    getfame(result)


if __name__=='__main__':
    pool = Pool(1)
    b=geturls()
    pool.map(main,b)