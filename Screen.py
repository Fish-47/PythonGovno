# coding=utf-8
from tkinter import *
from tkinter import ttk
import sys

root = Tk()
root.title("Screen")


root.geometry("350x250")


entry_width = Entry(root, width = 32)
entry_height = Entry(root , width = 32)
entry_width.pack()
entry_height.pack()


bttn_list = ["Изменить", "Закрыть",]



for i in bttn_list:
    rel = ""
    cmd=lambda x=i: widthSize(x)
    ttk.Button(root, text=i, command = cmd, width = 10).pack()


def widthSize(key):
    if key == "Изменить":
        w = entry_width.get()
        h = entry_height.get()
        a = str(w) + "x" + str(h)
        root.geometry(a)
        root.title(a)
    elif key == "Закрыть":
        sys.exit()


root.mainloop()