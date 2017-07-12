# coding:utf-8
from mod.Test import *
from mod.stock import *

def main():
    plist = []
    s = '''\
        imgInterpolation()
        image1()
        pltImage()
        plot6()
        pltAnotating()
        plotText()
        multipleFifures()
        plt2()
        plotDots()
        plotShow()
        beginPlot()
        getStockInfo()
        webScrape()
        countDownTime()
        monoColorPicturesShow()
        openCamera()
        #pushToGit() # THIS DOESN'T WORK!
        draw_with_cv()
        cvGo()
        nearestInterpolation()
        helloWorld()'''
    for i in s.split('\n'):
        plist.append(i.strip())    

    bgimg = np.zeros((540,960), np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for index, item in enumerate(plist):
        txt = "{}.{}".format(index, item)    
        cv2.putText(bgimg, txt, (35,index*20 + 20), font, 0.5, (200,200,20), 1)
        print index, item

    select = []
    wave = 0.9
    free = False
    while True:
        cv2.imshow("Program list", bgimg)
        key = cv2.waitKey(33) & 0xFF
        if key == 27: break
        elif key >=48 and key < 58:
            wave = 0.3
            ind = key - 48
            select.append(ind)
            free = True

        wave -= 0.03
        if wave <= 0 and free:            
            free = not free
            select.reverse()
            
            num = 0
            for i in range(len(select)):
                num += 10 ** (i) * select[i]

            os.system("cls")
            txt = "Selection: [{}]. Run Program: {}.{}".format(num, num, plist[num])
            mainInfo(txt)
            exec(plist[num])

            select = []




            

            #exec(plist[ind])

    cv2.destroyAllWindows()

if __name__ == '__main__':

    main()
    
    




    
    pass

'''
    install python
    add env variables: c:\python27;c:\python27\scripts;
    cmd >> 
        pip install numpy
        pip install mapplotlib

        download opencv3.2.0-vc14.exe
        extract, search cv2.pyd
        move it to python/Lib/site-packges/
        done!
        import cv2

    imwrite(filename, imgObj)


'''
