import sys
log = sys.stdout.write
import cv2
import numpy as np
import os





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
