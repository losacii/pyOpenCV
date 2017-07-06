import sys
log = sys.stdout.write
import cv2
import numpy as np
import os
import time, datetime

# to video tutorial 3

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
