# coding:utf-8
import os, time

orders = '''\
git add .
git commit -m 'update'
git push'''\
.split('\n')


for order in orders:
    print "\n\n>>>", order
    os.system(order)
    time.sleep(2.0)
    
time.sleep(3.5)
print "\n>>> update Done!\n"
time.sleep(2.5)
