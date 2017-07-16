# coding:utf-8
from mod.myMods import *
import cv2
import numpy as np
import datetime

def countDownTime():
    ''' 说明：倒计时
    '''
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = np.zeros((540,960), np.uint8)

    tput = raw_input("Enter Miinutes and Seconds, seperated with ' '\n> ").strip().split()
    tli = [0, 0, 0, 0]

    for i in range(len(tput)):
        tli[-i-1] = tput[-i-1]

    day, hr, min, sec = tli
    totalCount = int(day) * 24 * 3600 + int(hr) * 3600 + int(min) * 60 + int(sec)

    beginTime = time.time()
    while True:
        if cv2.waitKey(180) & 0xff == 27:
            break
        os.system("cls")

        timePassed = time.time() - beginTime
        if  timePassed > (totalCount):
            put("\nDone!", '\a' * 5)            
            break

        timeLeft = totalCount - timePassed
        tlli = []
        x, y = [int(i) for i in divmod(timeLeft, 3600 * 24)]
        tlli.append(x) # day
        x, y = [int(i) for i in divmod(y, 3600)]
        tlli.append(x) # hr
        x, y = [int(i) for i in divmod(y, 60)]
        tlli.append(x) # min
        tlli.append(y) # sec
        dayLeft, hrLeft, minLeft, secLeft = tlli
        
        txt = []
        if dayLeft > 0: txt.append("{} day(s)".format(dayLeft))
        if hrLeft > 0: txt.append(" {} hour(s)".format(hrLeft))
        if minLeft > 0: txt.append(" {} minute(s)".format(minLeft))
        txt.append((" {} second(s) left".format(secLeft)))
        
        tmpImage = cv2.imread("img/view.png")
        ptxt = ''.join(txt)
        cv2.putText(tmpImage, ptxt,(35,25), font, 0.5, (200,200,200,1), 1)
        cv2.imshow('Counting Down Time', tmpImage)

    cv2.destroyAllWindows()        


def cv_Draw():
    ''' 说明：绘制图形
    '''

    mainInfo("Drawing with OpenCV")
    img = np.zeros((540,960,3),np.uint8)

    # draw a line
    start = (20,350)
    end = (300,150)
    color = (255,0,0)
    lineWidth = 3
    cv2.line(img, start, end, color, lineWidth)

    # a rectangle
    topLeft = (20,60)
    bottomRight = (500,200)
    cv2.rectangle(img, topLeft, bottomRight, color, lineWidth)

    # circle
    center = (600, 240)
    radius = 60
    color = (0,255,0)
    lineWidth = -1
    cv2.circle(img, center, radius, color, lineWidth)

    # polygon
    point_list = [[10,5], [60,30], [90,20], [50,200]]
    pts = np.array(point_list, np.int32)
    cv2.polylines(img, [pts], True, (255,0,0), 5)

    # text
    pos = (50,270)
    pos2 = (800,270)
    lineWidth = 0.9
    thickness = 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV Tuts!', pos, font, lineWidth, (200,200,0), thickness, cv2.LINE_AA)

    cv2.line(img,pos,pos2,color,1)

    cv2.imshow('drawing',img)
    cv2.waitKey(int(20e3))
    cv2.destroyAllWindows()

def monoColorPicturesShow():
    ''' 说明：单色图片、时间显示
    '''
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = np.zeros((540,960), np.uint8)
    
    while True:
        img = np.zeros((540,960), np.float)

        showTime = time.strftime("%Y-%m-%d_%H:%M:%S")
        secDigits = datetime.datetime.now().microsecond.__str__()[:2]
        info = "{0}{1}.{2}".format('REC_', showTime, secDigits)

        cv2.putText(img, info,(35,25), font, 0.9, (200,60,100,1), 1)
        cv2.imshow('img', img)

        if 27 == (cv2.waitKey(20) & 0xff):
            break

    cv2.destroyAllWindows()


def cecordCamera():
    ''' 说明：打开视频或者摄像头，'s'键保存图片，'r'键录制/暂停(写入)
    '''

    cap = cv2.VideoCapture('video/split.avi')
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    vfileName = "C:\\vcap_" + time.strftime("%Y-%m-%d-%H%M%S") + ".mp4"

    wtr = cv2.VideoWriter(vfileName, fourcc, 20.0, (640,480))
    recordSwitch = False

    while True:
        ret, frame = cap.read()
        if frame is None:
            print "No image captured."
            continue

        if recordSwitch:
            wtr.write(frame)
            cv2.circle(frame, (30,30), 12, (0,0,200), -1)

        cv2.imshow('frame', frame)

        key = cv2.waitKey(20) & 0xff
        if key == 27:
            break
        elif key == ord('r'):
            recordSwitch = not recordSwitch
        elif key == ord('s'):
            imgName = 'C:/capImg_' + time.strftime("%Y-%m-%d-%H%M%S") + ".jpg"
            cv2.imwrite(imgName, frame)
            print imgName, "saved"
    wtr.release()
    cap.release()
    cv2.destroyAllWindows()
    print "file saved to :", vfileName

def cvOpenMedia():
    ''' 打开视频，播放视频
    '''
    cap = cv2.VideoCapture('video/split.avi')

    while True:
        ret, frame = cap.read()
        if frame is None:
            print "No frame captured now... sub Program End"
            break
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xff == 27:
            break

    cap.release(); print "Video released."
    cv2.destroyAllWindows()


def cvReadImage():
    ''' 读取、显示图片
    '''
    win1 = 'Read Image'

    img = cv2.imread("img/eyes.jpg")

    cv2.imshow(win1,img)
    cv2.waitKey(1000)

    cv2.destroyAllWindows()

    blit("\nopencv-version: ")
    blit(cv2.__version__)