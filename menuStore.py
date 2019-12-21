# coding=utf-8
from tkinter import *
from tkinter import ttk
import sys


def change_font(key):
    lbl.configure(font=("Arial", key))


def choose_font():
    lbl.configure(text='Выберите размер шрифта и нажмите на кнопку:')
    buttons['choose_fonts'].destroy()
    buttons['dont_choose_fonts'].destroy()
    for i, font in fonts.items():
        font.grid(column=0, row=i)
    buttons['click'].grid(column=0, row=i+1)


def clicked():
    for font in fonts.values():
        font.destroy()
    res = 'Для кого смотрим?'
    lbl.configure(text=res)
    buttons['click'].destroy()
    buttons['btn_boy'].grid(column=0, row=1)
    buttons['btn_girl'].grid(column=1, row=1)

def destroy_font_buttons():
    buttons['choose_fonts'].destroy()
    buttons['dont_choose_fonts'].destroy()
    buttons['click'].grid(column=0, row=1)

def child(boy=True):
    buttons['btn_boy'].destroy()
    buttons['btn_girl'].destroy()
    if boy:
        res = 'Для мальчика. Выберите категорию:'
        lbl.configure(text=res)
        buttons['btn_lego'].grid(column=0, row=1)
        buttons['btn_cars'].grid(column=1, row=1)
        buttons['btn_robots'].grid(column=2, row=1)
    else:
        res = 'Для девочки. Выберите категорию:'
        lbl.configure(text=res)


def lego():
    res = 'Lego'
    lbl.configure(text=res)
    buttons['btn_lego'].destroy()
    buttons['btn_cars'].destroy()
    buttons['btn_robots'].destroy()
    buttons['big_lego'].grid(column=0, row=1)
    buttons['small_lego'].grid(column=1, row=1)
    img_label.grid(column=0, row=2)


def cars():
    res = 'Cars'
    lbl.configure(text=res)
    buttons['btn_lego'].destroy()
    buttons['btn_cars'].destroy()
    buttons['btn_robots'].destroy()


def robots():
    res = 'Robots'
    lbl.configure(text=res)
    buttons['btn_lego'].destroy()
    buttons['btn_cars'].destroy()
    buttons['btn_robots'].destroy()
    buttons['bionicle'].grid(column=0, row=1)
    buttons['transformer'].grid(column=0, row=2)

def input_func(event):
    res = 'Введите фамилию студента:'
    lbl.configure(text=res)
    txt.grid(column=1, row=0)
    buttons['purchase'].grid(column=2, row=0)


def purchase(text, btn):
    lbl.configure(text='Ctrl+Q чтобы перейти к оплате')
    for key, btn in buttons.items():
        if key not in ['purchase', 'close']:
            btn.destroy()
    frame.grid(column=0, row=1)

def done():
    lbl.configure(text='Оплачено, {txt.get()}!')
    buttons['purchase'].destroy()
    txt.destroy()
    buttons['close'].grid(column=0, row=1)

def close():
    window.destroy()

window = Tk()
window.title('Toys Catalog')
window.geometry('700x250')
lbl = Label(window, text="Добро пожаловать в каталог детских игрушек.зменить размер шрифта?")
lbl.grid(column=0, row=0)
# txt.grid(column=1, row=0)
buttons = {}
buttons['choose_fonts'] = Button(window, text="Р”Р°", command=choose_font)
buttons['dont_choose_fonts'] = Button(window, text="РќРµС‚", command=destroy_font_buttons)
buttons['choose_fonts'].grid(column=0, row=1)
buttons['dont_choose_fonts'].grid(column=1, row=1)
buttons['click'] = Button(window, text='Перейти к выбору игрушек', command=clicked)
frame = Frame(window, width=10)
frame.bind('<Control-q>', input_func)
frame.focus_set()
buttons['btn_boy'] = Button(window, text="Мальчик")
buttons['btn_boy']['command'] = lambda boy=True: child(boy=True)
buttons['btn_girl'] = Button(window, text="Девочка")
buttons['btn_girl']['command'] = lambda boy=False: child(boy=False)
buttons['btn_lego'] = Button(window, text="Lego", command=lego)
buttons['btn_cars'] = Button(window, text="Cars", command=cars)
buttons['btn_robots'] = Button(window, text="Robots", command=robots)
buttons['big_lego'] = Button(window, text="Большой: 12000 р.")
buttons['big_lego']['command'] = lambda a=1: purchase(text="Большой Lego: 12000 р.", btn='big_lego')
buttons['small_lego'] = Button(window, text="РњР°Р»РµРЅСЊРєРёР№: 1000 СЂ.")
buttons['small_lego']['command'] = lambda a=1: purchase(text="Маленький Lego: 1000 р.", btn='small_lego')
buttons['bionicle'] = Button(window, text="Bionicle: 1600 СЂ.")
buttons['bionicle']['command'] = lambda a=1: purchase(text="Bionicle: 1600 СЂ.", btn='bionicle')
buttons['transformer'] = Button(window, text="Трансформер: 1500 р.")
buttons['transformer']['command'] = lambda a=1: purchase(text="Трансформер: 1500 р.", btn='transformer')
buttons['purchase'] = Button(window, text="Оплатить", command=done)
buttons['close'] = Button(window, text="Закрыть", command=close)

fonts = {i: Checkbutton(window, text=str(i), command=lambda a=1: change_font(i)) for i in range(10, 35, 5)}
txt = Entry(window, width=10)
window.mainloop()