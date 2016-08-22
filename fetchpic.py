import urllib.request
import urllib.parse

website = 'http://images.dmzj.com/x/%E5%B9%B8%E8%BF%90%E6%98%9F/%E7%AC%AC8%E5%8D%B7/011.jpg'
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
header= {
    'User-Agent':useragent,
    'Referer':'http://manhua.dmzj.com/xingyunxing/15718.shtml'
}
req=urllib.request.Request(url=website,data=None,headers=header)
response=urllib.request.urlopen(req).read()
file=open("test.jpg","wb")
file.write(response)
file.close()