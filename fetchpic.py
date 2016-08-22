import urllib.request
import urllib.parse
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
header= {
    'User-Agent':useragent,
    'Referer':'http://manhua.dmzj.com/xingyunxing/19048.shtml'
}
for i in range(0,75):
    if i in range(0,10):
        website = 'http://images.dmzj.com/x/%E5%B9%B8%E8%BF%90%E6%98%9F/%E7%AC%AC09%E5%8D%B7/00'+str(i)+'.jpg'
    else:
         website = 'http://images.dmzj.com/x/%E5%B9%B8%E8%BF%90%E6%98%9F/%E7%AC%AC09%E5%8D%B7/0'+str(i)+'.jpg'
    req=urllib.request.Request(url=website,data=None,headers=header)
    response=urllib.request.urlopen(req).read()
    if i in range(0,10):
        filename='00'+str(i)+'.jpg'
    else:
        filename='0'+str(i)+'.jpg'
    file=open(filename,"wb")
    file.write(response)
    file.close()
    print("done"+str(i)+'\n')