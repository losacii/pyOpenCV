# coding:utf-8
from mod.myMods import *
from mod.tk_Examples import *
from mod.pyBasic import *
from mod.cvMod import *
from mod.webBasics import *
from mod.plotBasics import *


def runFunction(event, afunc):
    exec(afunc)

class PBtn:

    def __init__(self, master, txt, program):

        self.Btn = Button(master, text=txt)
        self.Btn.bind('<Button-1>', lambda x: runFunction(x, program))
        self.Btn.pack(fill=X)

    def bind(self, key, program):
        self.Btn.bind(key, lambda x: runFunction(x, program))


def main():
    root = Tk()
    root.minsize(580,360)

    frameBasic = Frame(root) # an invisible container
    frameBasic.pack(side=LEFT)
    PBtn(frameBasic, "sayHello", "sayHello('John Berry')")
    PBtn(frameBasic, "RE : split test", "testReSplit()")
    PBtn(frameBasic, "字符编码", "UnicodeToUtf8()")
    x = PBtn(frameBasic, "鼠标左右键绑定", "mainInfo('Hello World!!!!!')")
    x.bind('<Button-3>', "sayHello('Mickey')")

    frameOpenCV = Frame(root,width=800)
    frameOpenCV.pack(side=LEFT)
    PBtn(frameOpenCV, "cv2: 读取、显示图片", "cvReadImage()")
    PBtn(frameOpenCV, "cv2: 读取、播放视频", "cvOpenMedia()")
    PBtn(frameOpenCV, "cv2: 录制视频", "cecordCamera()")
    PBtn(frameOpenCV, "cv2: 单色图片、时间显示", "monoColorPicturesShow()")
    PBtn(frameOpenCV, "cv2: 绘制图形", "cv_Draw()")
    PBtn(frameOpenCV, "cv2: 倒计时", "countDownTime()")

    frameTkinter = Frame(root)
    frameTkinter.pack(side=LEFT)
    PBtn(frameTkinter, "Tkinter: lables on root window", "tk_lables()")
    PBtn(frameTkinter, "Tkinter: Frame,Buton的布局", "TK__frames_buttons()")
    PBtn(frameTkinter, "Tkinter: grid_layout()", "TK_grid_layout()")
    PBtn(frameTkinter, "Tkinter: TK_Menus()", "TK_Menus()")
    PBtn(frameTkinter, "Tkinter: TK_listitems()", "TK_listitems()")
    PBtn(frameTkinter, "Tkinter: ", "")
    PBtn(frameTkinter, "Tkinter: ", "")    

    framePlot = Frame(root)
    framePlot.pack(side=LEFT)
    PBtn(framePlot, "Plot: simple Plot", "beginPlot()")
    PBtn(framePlot, "Plot: 画点", "plotDots()")
    PBtn(framePlot, "Plot: 线条点样式", "plt2()")
    PBtn(framePlot, "Plot: 正弦、余弦曲线", "plotShow()")
    PBtn(framePlot, "Plot: 多幅图片", "multipleFifures()")
    PBtn(framePlot, "Plot: 文字、直方图", "plotText()")
    PBtn(framePlot, "Plot: 注解", "pltAnotating()")
    PBtn(framePlot, "Plot: plot6()", "plot6()")
    PBtn(framePlot, "Plot: pltImage()", "pltImage()")
    PBtn(framePlot, "Plot: imageHisto()", "imageHisto()")
    PBtn(framePlot, "Plot: 图像增强", "imageEnhance()")
    PBtn(framePlot, "Plot: imgInterpolation()", "imgInterpolation()")
    PBtn(framePlot, "Plot: nearestInterpolation()", "nearestInterpolation()")

    frameWeb = Frame(root)
    frameWeb.pack(side=LEFT)
    PBtn(frameWeb, "Web: 网页内容提取", "webScrape()")
    PBtn(frameWeb, "Web: StockInfo", "getStockInfo()")    

    root.mainloop()

if __name__ == '__main__':
    main()

    print "\n\n----- Exit! -----"