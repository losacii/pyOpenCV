# coding:utf-8
from mod.myMods import *
from Tkinter import *

def TK_listitems():
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
        print "Sure, it works.", time.strftime("%Y-%m-%d-%H%M%S")

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


def TK_grid_layout():
    root = Tk()
    root.minsize(300,300)

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

def TK__frames_buttons():
    root = Tk() 
    root.minsize(600,300)

    frameA = Frame(root) # an invisible container
    frameA.pack(side=LEFT)

    frameB = Frame(root,width=800)
    frameB.pack(side=LEFT)

    btn1 = Button(frameA, text="Button One", fg="red")
    btn2 = Button(frameA, text="Button Two", fg="blue")
    btn3 = Button(frameA, text="Button Three", fg="green")
    btn1.pack(side=TOP, fill=X)
    btn2.pack(side=TOP, fill=X)
    btn3.pack(side=TOP, fill=X)

    btn4 = Button(frameB, text="Button Four", fg="purple")
    btn5 = Button(frameB, text="Button Five: Hello World, Welcome!", fg="purple")
    btn6 = Button(frameB, text="Button6", fg="purple")
    btn4.pack(side=TOP, fill=X)
    btn5.pack(side=TOP, fill=X)
    btn6.pack(side=TOP, fill=X)

    root.mainloop()

def tk_lables():
    root = Tk()
    root.minsize(200,200)

    lb1 = Label(root, text="Hello World!", bg="blue", fg='yellow')
    lb1.pack()

    root.mainloop()
