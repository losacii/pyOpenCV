# -*- coding: UTF-8 -*-
from Tkinter import *
import time


def TK_listitems():
    from Tkinter import *           # 导入 Tkinter 库
    root = Tk()                     # 创建窗口对象的背景色
                                    # 创建两个列表
    li     = ['C','python','php','html','SQL','java']
    movie  = ['CSS','jQuery','Bootstrap']
    listb  = Listbox(root)          #  创建两个列表组件
    listb2 = Listbox(root)
    for item in li:                 # 第一个小部件插入数据
        listb.insert(0,item)

    for item in movie:              # 第二个小部件插入数据
        listb2.insert(0,item)

    listb.pack()                    # 将小部件放置到主窗口中
    listb2.pack()
    root.mainloop()                 # 进入消息循环


def TK_Menus():

    def doNothing():
        print "Haha! Nothing happens here!", time.strftime("%Y-%m-%d-%H%M%S")

    root = Tk()

    top_menu = Menu(root)
    root.config(menu=top_menu)

    subMenuA = Menu(top_menu) # within
    top_menu.add_cascade(label="File", menu=subMenuA)

    subMenuA.add_command(label="New Project ...", command=doNothing)
    subMenuA.add_command(label="Open ...", command=doNothing)
    subMenuA.add_separator()
    subMenuA.add_command(label="Save as ...", command=doNothing)
    subMenuA.add_command(label="Exit ...", command=doNothing)

    editMenu = Menu(top_menu)
    top_menu.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Redo", command=doNothing)

    root.mainloop()


class MyButton:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print my button", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print "Wow, button clicked, it works!"

def btnClass():
    root = Tk()

    btn = MyButton(root)
    btn2 = MyButton(root)
    btn3 = MyButton(root)

    root.mainloop()

def TK_button_call1():
    root = Tk()

    def leftClick(event):
        print "Left!"
    def middleClick(event):
        print "Middle!"
    def rightClick(event):
        print "Right!"

    frame = Frame(root, width=640, height=360) # an invisible frame
    frame.bind("<Button-1>", leftClick)
    frame.bind("<Button-2>", middleClick)
    frame.bind("<Button-3>", rightClick)
    frame.pack()

    root.mainloop()
    root.destroy()

def TK_button_call():
    root = Tk()

    def printName(event):
        print("Hello my name is Bucky!")

    btn1 = Button(root, text="click this!")
    btn1.bind("<Button-3>", printName) # mouse-left click: 1=left, 2=middle, 3=right
    btn1.pack()

    root.mainloop()

def TK_grid_layout():
    root = Tk()

    label_1 = Label(root, text="Name",fg='red',bg='grey')
    label_2 = Label(root, text="Passwd")
    entry_1 = Entry(root)
    entry_2 = Entry(root)

    label_1.grid(row=0, sticky=E) # Ease, North, West, South
    label_2.grid(row=1, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)

    ck = Checkbutton(root, text="Keep me logged in")
    ck.grid(columnspan=2)

    root.mainloop()

def TK_LablePostion():
    root = Tk()

    label_1 = Label(root, text="ONE", bg='white')
    label_1.pack()
    label_2 = Label(root, text="TWO", bg='black', fg='green')
    label_2.pack(fill=X)
    label_3 = Label(root, text="THREE", bg='blue', fg='white')
    label_3.pack(fill=Y, side=LEFT)

    root.mainloop()

def TK__frames_buttons():
    root = Tk() 

    topFrame = Frame(root) # an invisible container
    topFrame.pack()

    bottomFrame = Frame(root,width=800)
    bottomFrame.pack(side=BOTTOM)

    btn1 = Button(topFrame, text="Button One", fg="red")
    btn2 = Button(topFrame, text="Button Two", fg="blue")
    btn3 = Button(topFrame, text="Button Three", fg="green")
    btn4 = Button(bottomFrame, text="Button Four", fg="purple")
    btn5 = Button(bottomFrame, text="Button Five: Hello World, Welcome!", fg="purple")
    btn6 = Button(bottomFrame, text="Button6", fg="purple")

    btn1.pack(side=LEFT)
    btn2.pack(side=LEFT)
    btn3.pack(side=LEFT)
    btn4.pack(side=BOTTOM)
    btn5.pack(side=BOTTOM)
    btn6.pack(side=BOTTOM)

    root.mainloop()

def TK_SimpleWindow():
    root = Tk() # a blank window
    lb = Label(root, text="Just a simple label")
    lb.pack()
    root.mainloop()


