import sys
log = sys.stdout.write
import os
import random
import cv2
import numpy as np

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
'''
