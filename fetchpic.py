import urllib.request
import urllib.parse
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
header= {
    'User-Agent':useragent,
    'Referer':'http://manhua.dmzj.com/nietaxianjing/34281.shtml'
}
yeshu = input("yeshu:\n")
for i in range(1,int(yeshu)+1):
    if i in range(1,10):
        website= 'http://images.dmzj.com/n/%E6%8D%8F%E9%80%A0%E9%99%B7%E9%98%B1/%E7%AC%AC03%E8%AF%9D_1426930575/0'+str(i)+'.jpg'
    else:
        website= 'http://images.dmzj.com/n/%E6%8D%8F%E9%80%A0%E9%99%B7%E9%98%B1/%E7%AC%AC03%E8%AF%9D_1426930575/'+str(i)+'.jpg'
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