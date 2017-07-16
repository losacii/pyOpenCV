from mod.myMods import *


def UnicodeToUtf8():
    ''' unicode     ---encode--->   gbk / utf8
        gbk / utf8  ---decode--->   unicode
    '''
    x = 19990
    while x < 20300:
        print "{}{}{}     ".format(x, '-->', unichr(x).encode('gbk')),
        if x % 5 == 0:
            print
        x += 1
    

def testReSplit():
    print re.split(",\s*", "1,2,3, 4,  5,    6, 7")

def sayHello(name):
    print "Hello World!"
    print "Welcome {}\n".format(name)


