from mod.myMods import *


def getStockInfo():
    font = cv2.FONT_HERSHEY_SIMPLEX
    url = 'http://hq.sinajs.cn/list=s_sh000001'

    while True:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request) 
        value = response.read().split(',')[1]
    
        tm = time.strftime("%Y-%m-%d %H : %M : %S")
        txt = "SH INDEX: " + str(value)

        img = np.zeros((200,600),np.uint8)
        cv2.putText(img,tm, (20,50),font, 0.5, (255,255,0), 1)
        cv2.putText(img,txt, (20,30),font, 0.5, (255,255,0), 1)

        cv2.imshow("img", img)
        if cv2.waitKey(50) & 0xff == 27:
            break

    cv2.destroyAllWindows()
    print "stock info quit."


def webScrape():
    regex = '<p>(.+?)</p>'
    patt = re.compile(regex)

    webfile = urllib2.urlopen("http://www.sohu.com/a/155964201_114988?_f=index_news_1")
    txt = webfile.read()
    for i in re.findall(patt, txt):
        print i.decode("utf-8")
        print 
