# coding:utf-8
import os
import sys
import time
import random
import urllib2
import re
import cv2
import numpy as np
import matplotlib.pyplot as plt


def mainInfo(title):
    ''' 说明： 主窗口信息，矩形信息界面
    '''
    os.system("cls")
    aline()
    print
    put(str(title).center(80)); put('\n')
    print
    aline()
    pass

def aline():
    ''' 说明： 输出一行分割线
              > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >
    '''
    for _ in range(8):
        time.sleep(0.03)
        put(" >" * 5)
    put('\n')

def blit(s):
    ''' 说明：输出字符串，遇到空格停顿，达到打字动画效果
    '''
    for i in s:
        put(i)
        if i is ' ' or i is '\n':
            time.sleep(0.03)

def put(*li):
    ''' 举例： put(1,2,3,4,"hello", " World!")
    '''
    for i in li:
        sys.stdout.write(str(i))
