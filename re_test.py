#__author__=''
# -*- coding:utf-8 -*-
import re
import requests
import os
from multiprocessing import Pool

def getPage(url):
    # 获取页面信息
    # 构造页面请求
    #url = 'http://www.dy2018.com/html/gndy/dyzz/index.html'
    page = 'http://www.dy2018.com'
    html_url=[]
    #s=range(2,295)
    response = requests.get(url)
    #print response.status_code,response.headers['content-type'],response.encoding,response.content
    #response.encoding='GB2312'
    dytext = response.text
    pattern=re.compile(r'<b>.*?<a.*?href="(.*?)".*?</b>',re.S)
    result = re.findall(pattern, dytext)
    for m in result:
        html_url.append(page+m)
        #print html_url
    return html_url
def getfame(html_url):
    for u in html_url:
        res=requests.get(u)
        res.encoding='gb2312'
        ftext=res.text
        #ftext.encode('gb2312','ignore')
        #print ftext
        pat=re.compile(r'<!--Content Start-->.*?<p>.*?<img src=".*?alt.*?</p>.*?<p(.*?)</p>.*?<!--xunleiDownList Start-->.*?<td style="WORD-WRAP.*?<a href="(.*?)">ftp://',re.S)
        resu=re.findall(pat,ftext)
        for i in resu:
            print i[0]
            f = open('dygod.txt', 'a+')
            f.write(i[0].encode('gbk','ignore')+'  '+i[1].encode('gbk','ignore')+'\n')
            f.flush()
            f.close()

def main(b):

    for a in b:
        if a==1:
            print '下载第：'+str(a)+'页'
            url = 'http://www.dy2018.com/html/gndy/dyzz/index.html'
            html_url=getPage(url)
            getfame(html_url)
        else:
            print '下载第：' + str(a) + '页'
            print 'http://www.dy2018.com/html/gndy/dyzz/index_'+str(a)+'.html'
            html_url=getPage('http://www.dy2018.com/html/gndy/dyzz/index_'+str(a)+'.html')
            getfame(html_url)

if __name__=='__main__':
    pool = Pool(4)
    x=range(1,295)
    for i in x:
        pool.map(main,x)