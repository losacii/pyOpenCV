# coding:utf-8
import os, time

orders = '''\
git add .
git commit -m 'update'
git push'''.split('\n')



for i in orders:
    print i
