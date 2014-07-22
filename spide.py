#这个是我在群里看到的,有人问爬虫全局代理有人给个代码,记录以下  
###############
#采集代理信息
proxy_txt = open('proxy_list.txt','w')
proxy_tr = re.compile("(?isu)<tr[^>]*>(.*?)</tr>")
proxy_td = re.compile("(?isu)<td[^>]*>(.*?)</td>")
#UA模拟
proxy_ua = {'User-Agent:':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
#Request连接网页
proxy_url = urllib2.Request(url='http://www.site-digger.com/html/articles/20110516/proxieslist.html',headers=proxy_ua)
#写入代理并检测是否成功
try:
    GetProxy = urllib2.urlopen(proxy_url)
    HtmlRead = GetProxy.read()
#如果错误
except Exception:
    print '-'*50
    print '采集代理错误，请检查您的网络是否正常！'
    print '-'*50
    raw_input('按回车结束程序:')
#没有错误继续执行
else:
    #遍历所有网页找到规则并读取
    for row in proxy_tr.findall(HtmlRead):
        for col in proxy_td.findall(row)[:1]:
            #代理信息写入文件
            proxy_txt.write(col+'\n')
    proxy_txt.close()

print '-'*20+'获取代理完毕'+'-'*20
################################### 采集代理结束 ##############################
