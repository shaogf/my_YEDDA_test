import tkinter as tk
from tkinter import *

#label标签
# win = tk.Tk()
# win.title('sunk')
# win.geometry("400x400+200+20")
#
# label1 = tk.Label(win,text = 'good',bg = 'pink')
# label2 = tk.Label(win,text = 'nice',bg = 'green')
# label3 = tk.Label(win,text = 'cool',bg = 'red')
# label4 = tk.Label(win,text = 'test',bg = 'yellow')
# label5 = tk.Label(win,text = 'head',bg = 'blue')
# #绝对布局
# label4.place(x = 60,y = 60)
# #相对布局
# label1.pack(fill = tk.BOTH,side = tk.LEFT)
# label2.pack(fill = tk.BOTH,side = tk.TOP)
# label3.pack(fill = tk.BOTH,side = tk.BOTTOM)#将标签填充满，side：控制位置
# #表格布局
# label1.grid(row = 1,column = 1)
# label2.grid(row = 1,column = 0)
# label3.grid(row = 0,column = 1)
# label4.grid(row = 0,column = 0)
#label,scale,button
# def resize(event = None):
#     label.config(font="Helvetica -%d bold" % scale.get())
# win = tk.Tk()
# win.geometry("250x150")
# label = Label(win,text = 'hello world',font = 'Helvetica -12 bold')
# label.pack(fill = BOTH,expand = 1)
# scale = Scale(win,from_ = '10',to = '40',orient = HORIZONTAL,command = resize)#HORIZONTAL：水平
# scale.pack(fill = BOTH,expand = 1)
# scale.set(12)
#
# quit = Button(win,text = 'quit',command = win.quit,activeforeground = 'white',activebackground = 'red')
# quit.pack()
#复选框
# def updata():
#     message = ""
#     if hobby1.get() == True:
#         message += "money is YES\n"
#     if hobby2.get() == True:
#         message += "power is YES\n"
#     if hobby3.get() == True:
#         message += "people is YES\n"
#     #清除text上的内容
#     text.delete(0.0,tk.END)#删除文本框的原始内容
#     text.insert(tk.INSERT,message)#将message的内容插入文本框
# hobby1 = tk.BooleanVar()
# check1 = tk.Checkbutton(win,text = 'money',variable = hobby1,command = updata)#variable：变量
# check1.pack()
#
# hobby2 = tk.BooleanVar()
# check2 = tk.Checkbutton(win,text = 'power',variable = hobby2,command = updata)
# check2.pack()
#
# hobby3 = tk.BooleanVar()
# check3 = tk.Checkbutton(win,text = 'people',variable = hobby3,command = updata)
# check3.pack()
#
# text = tk.Text(win,width = 50,height = 5)#文本框
# text.pack()
#框架控件
# frm = tk.Frame(win)
# frm.pack()
# #left
# frm_1 = tk.Frame(frm)
# tk.Label(frm_1,text = '左上',bg = 'pink').pack(side = tk.TOP)
# tk.Label(frm_1,text = '左下',bg = 'blue').pack(side = tk.TOP)
# frm_1.pack(side = tk.LEFT)
#
# frm_2 = tk.Frame(frm)
# tk.Label(frm_2,text = '右上',bg = 'red').pack(side = tk.TOP)
# tk.Label(frm_2,text = '右下',bg = 'green').pack(side = tk.TOP)
# frm_2.pack(side = tk.RIGHT)
#列表框
#创建一个listbox,添加几个元素
#SINGLE与BORWSE类似，但是不支持鼠标移动选中位置
# lb = tk.Listbox(win,selectmode = tk.BROWSE)#允许鼠标移动选中位置
# lb.pack()
# for i in ['good','nice','handsome','cool']:
#     #按顺序添加
#     lb.insert(tk.END,i)
# lb.insert(tk.ACTIVE,'cool')
# lb.insert(tk.END,['very good','very cool'])
# lb.delete(1,2)#删除good ,nice
# lb.select_set(1,2)#默认选中序列1，2
# print(lb.size())
# print(lb.get(2,3))#cool,'very good','very cool'
# print(lb.curselection())#返回被select_set()设置的元素的索引
# print(lb.select_includes(1))#判断一个选项是否被选中
# print(lb.select_includes(2))
# lb = tk.Listbox(win,selectmode = tk.EXTENDED) #EXTENDED可以使listbox支持shift和ctrl,按shift可以连续选，ctrl可以多选
# lb.pack()
# for i in ["good", "nice", "handsome", "vg", "vn",
#             "good2", "nice3", "handsome4", "vg5", "vn4",
#             "good3", "nice4", "handsome44", "vg5", "vn6"
#              ]:
#     lb.insert(tk.END,i)
# #加滚动条
# sc = tk.Scrollbar(win)
# sc.pack(side = tk.RIGHT,fill = tk.Y)
# lb.configure(yscrollcommand = sc.set())
#
# win.mainloop()

#coding:utf-8

def bag(n, c, w, v):
    """
    测试数据：
    n = 6  物品的数量，
    c = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1]:
                value[i][j] = max(value[i-1][j],value[i - 1][j - w[i - 1]] + v[i - 1])
    for x in value:
        print(x)
    return value

def show(n, c, w, value):
    print('最大价值为:', value[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i+1, '个,', end='')

def bag1(n, c, w, v):
    values = [0 for i in range(c+1)]
    for i in range(1, n + 1):
        for j in range(c, 0, -1):
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i-1]:
                values[j] = max(values[j-w[i-1]]+v[i-1], values[j])
    return values


if __name__ == '__main__':
    n = 6
    c = 10
    w = [2, 2, 3, 1, 5, 2]
    v = [2, 3, 1, 5, 4, 3]
    value = bag(n, c, w, v)
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    # [0, 0, 3, 3, 5, 5, 5, 5, 5, 5, 5]
    # [0, 0, 3, 3, 5, 5, 5, 6, 6, 6, 6]
    # [0, 5, 5, 8, 8, 10, 10, 10, 11, 11, 11]
    # [0, 5, 5, 8, 8, 10, 10, 10, 12, 12, 14]
    # [0, 5, 5, 8, 8, 11, 11, 13, 13, 13, 15]
    show(n, c, w, value)
    # 最大价值为: 15
    # 背包中所装物品为:
    # 第 2 个,第 4 个,第 5 个,第 6 个,
    print('\n空间复杂度优化为N(c)结果:', bag1(n, c, w, v))
    #空间复杂度优化为N(c)结果: [0, 5, 5, 8, 8, 11, 11, 13, 13, 13, 15]