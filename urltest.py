import urllib
zhang = raw_input("zhangjie\n")
zong = input("yeshu\n")
for i in range(0,int(zong)):
    website="http://59.53.67.165:8080/comicdata/11004/"+str(zhang)+'/'+str(i)+".jpg"
    urllib.urlretrieve(website,str(i)+".jpg")
    print("done"+str(i)+'\n')