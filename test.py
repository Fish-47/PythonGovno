# coding=utf-8
from tkinter import *
from tkinter import ttk
import math
import sys

root = Tk()
root.title("Dublicate")
root.geometry("600x250")
label1 = Label(text="0", fg="#eee", bg="#333")
bttn_list = [
"3", "47", "304",
"5691",  "Очистить",
"Exit", "Дублировать",]

r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)

def calc(key):
    global memory
    if key == "Очистить":
        calc_entry.delete(0, END)
    elif key == "Exit":
        root.after(1, root.destroy)
        sys.exit()
    elif key == "Дублировать":
        calc_entry.insert(END, END)
    else:
        calc_entry.insert(END, key)

root.mainloop()