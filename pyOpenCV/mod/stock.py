# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

def nearestInterpolation():
    from PIL import Image
    img = Image.open('img/stinkbug.png')
    img.thumbnail((64, 64), Image.ANTIALIAS) # resizes image in-place

    plt.figure()

    plt.subplot(2,1,1)
    imgplot = plt.imshow(img, interpolation="nearest")

    plt.subplot(2,1,2)
    imgplot = plt.imshow(img, interpolation="bicubic")

    plt.show()

def imgInterpolation():
    '''Interpolation calculates what the color or value of a pixel “should” be, 
    according to different mathematical schemes. 
    One common place that this happens is when you resize an image.
    '''
    from PIL import Image
    img = Image.open('img/stinkbug.png')
    img.thumbnail((64, 64), Image.ANTIALIAS) # resizes image in-place
    imgplot = plt.imshow(img)
    plt.show()


def image1():
    import matplotlib.image as mpimg
    img=mpimg.imread('img/stinkbug.png')
    lum_img = img[:,:,0]  
    

    plt.figure()
    plt.subplot(2,2,1)
    imgplot = plt.imshow(lum_img, clim=(0.2, 0.7))

    plt.show()

def imageHisto():
    import matplotlib.image as mpimg
    img=mpimg.imread('img/stinkbug.png')
    lum_img = img[:,:,0]
    plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

    plt.show()

def pltImage():
    import matplotlib.image as mpimg
    img=mpimg.imread('img/stinkbug.png')
    

    plt.figure()
    plt.subplot(2,2,1)
    imgplot = plt.imshow(img)

    plt.subplot(2,2,2)
    lum_img = img[:,:,0]
    imgplot = plt.imshow(lum_img)

    plt.subplot(2,2,3)
    plt.imshow(lum_img, cmap="hot")

    plt.subplot(2,2,4)
    plt.imshow(lum_img)
    imgplot.set_cmap('nipy_spectral')
    plt.colorbar()


    plt.show()



def plot6():
    from matplotlib.ticker import NullFormatter  # useful for `logit` scale

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # make up some data in the interval ]0, 1[
    y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    y = y[(y > 0) & (y < 1)]
    y.sort()
    x = np.arange(len(y))

    # plot with various axes scales
    plt.figure(1)

    # linear
    plt.subplot(221)
    plt.plot(x, y)
    plt.yscale('linear')
    plt.title('linear')
    plt.grid(True)


    # log
    plt.subplot(222)
    plt.plot(x, y)
    plt.yscale('log')
    plt.title('log')
    plt.grid(True)


    # symmetric log
    plt.subplot(223)
    plt.plot(x, y - y.mean())
    plt.yscale('symlog', linthreshy=0.01)
    plt.title('symlog')
    plt.grid(True)

    # logit
    plt.subplot(224)
    plt.plot(x, y)
    plt.yscale('logit')
    plt.title('logit')
    plt.grid(True)
    # Format the minor tick labels of the y-axis into empty strings with
    # `NullFormatter`, to avoid cumbering the axis with too many labels.
    plt.gca().yaxis.set_minor_formatter(NullFormatter())
    # Adjust the subplot layout, because the logit one may take more space
    # than usual, due to y-tick labels like "1 - 10^{-3}"
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)

    plt.show()

def pltAnotating():
    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.01),
                )

    plt.ylim(-2,2)
    plt.show()

def plotText():
    
    # Fixing random state for reproducibility
    np.random.seed(19680802)

    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()

def multipleFifures():
    def f(t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)

    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k') # 'k' means normal?

    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

    plt.show()

def plotShow():

    X = np.linspace(-2 * np.pi, 2 * np.pi, 256)
    Ysin = np.sin(2 * X)
    Ycos = np.cos(X)

    plt.figure()
    plt.plot(X, Ysin)
    plt.plot(X, Ycos, linewidth=3.0, alpha=0.8)

    plt.show()




def plt2():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()


def plotDots():
    plt.plot([1,2,3,4], [1,4,9,16], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()

def beginPlot():
    plt.plot([1,2,3,4,5,2,4])
    plt.ylabel('some numbers')
    plt.show()


