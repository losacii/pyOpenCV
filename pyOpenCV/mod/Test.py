# -*- coding: utf-8 -*-
import sys
log = sys.stdout.write
import cv2
import numpy as np
import os
import time, datetime
import urllib2
import re

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
    print "EXIT!"



def webScrape():
    regex = '<p>(.+?)</p>'
    patt = re.compile(regex)

    webfile = urllib2.urlopen("http://www.sohu.com/a/155964201_114988?_f=index_news_1")
    txt = webfile.read()
    for i in re.findall(patt, txt):
        print i.decode("utf-8")
        print 

# Functions go here!
def put(*li):
    for i in li:
        sys.stdout.write(str(i))
        sys.stdout.flush()

def beeps():
    for _ in range(5):
        put('\a')
        time.sleep(0.03)

def countDownTime():
    tmp = raw_input("Enter Miinutes and Seconds, seperated with ' '\n> ").strip().split()
    if len(tmp) == 1:
        sec =  int(tmp[0])
        hr = min = 0
    elif len(tmp) == 2:
        min, sec = [int(i) for i in tmp]
        hr = 0
    elif len(tmp) == 3:
        hr, min, sec = [int(i) for i in tmp]

    totalCount = hr * 3600 + min * 60 + sec
    beginTime = time.time()
    while True:
        timePassed = time.time() - beginTime
        if  timePassed > (totalCount):
            print "\n\nDone!"
            beeps()
            print len(sys.argv), sys.argv
            break
        os.system("cls")
        secsLeft = totalCount - timePassed
        h = secsLeft // 3600
        m = (secsLeft - 3600 * h) // 60
        s = secsLeft % 60
        put("TIME LEFT: {} - {} - {}".format(h, m, round(s)))
        time.sleep(0.99)

def draw_with_cv():
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
    lineWidth = 0.5
    thickness = 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV Tuts!', pos, font, lineWidth, (200,200,0), thickness, cv2.LINE_AA)

    cv2.line(img,pos,pos2,color,1)

    cv2.imshow('drawing',img)
    cv2.waitKey(int(20e3))
    cv2.destroyAllWindows()


def monoColorPicturesShow():
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = np.zeros((540,960), np.uint8)
    
    while True:

        showTime = time.strftime("%Y-%m-%d_%H:%M:%S")
        secDigits = datetime.datetime.now().microsecond.__str__()[:2]
        info = "{0}{1}.{2}".format('REC_', showTime, secDigits)
        img = np.zeros((540,960), np.float)
        cv2.putText(img, info,(35,25), font, 0.5, (200,60,100,1), 1)
        cv2.imshow('img', img)

        if 27 == (cv2.waitKey(20) & 0xff):
            break

    cv2.destroyAllWindows()

def cecordCamera():

    cap = cv2.VideoCapture('split.avi')
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

    while True:
        ret, frame = cap.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        out.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xff == 27:
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()

def openCamera():

    cap = cv2.VideoCapture('split.avi')

    while True:
        ret, frame = cap.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xff == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


def pushToGit():
    print "Executing os commands:"
    os.system("dir")
    os.system("git init")
    print "Done!"
    
def helloWorld():
    print "Hello World!\n"

def cvGo():
    win1 = 'Black Rect'

    img0 = cv2.imread("c:/pic/color.png")
    img1 = np.zeros((540,960),float)
    img2 = cv2.imread("c:/pic/f22.jpg",cv2.IMREAD_GRAYSCALE)

    cv2.imshow(win1,img0)
    cv2.waitKey()

    cv2.imshow(win1,img1)
    cv2.waitKey()

    cv2.imshow(win1,img2)
    cv2.waitKey()

    cv2.destroyAllWindows()

    log("opencv-version: ")
    log(cv2.__version__)

    print "\n\n--- PRESS ENTER TO CONTINUE ---\n"
    
def helloNumbers():
    for i in range(10):
        print i


def aline():
    for _ in range(8):
        time.sleep(0.1)
        log(" >" * 5)
    log('\n')

def mainInfo(title):
    aline()
    print
    log(str(title).upper().center(80)); log('\n')
    print
    aline()
    pass
