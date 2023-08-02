import random
from tkinter import *
import sys
from PIL import Image
import os


def restart_program(): #новая генерация (перезагрузка)
    python = sys.executable
    os.execl(python, python, * sys.argv)


def coins(): #подброс монетки
    coin = random.choice(range(0, 10000)) % 2 == 0
    return coin


def kubik(): #подброс кубика
    return(int(random.randint(1, 6)))


def start_zone(): #определение стартовой зоны
    money = coins(), coins()
    if money[0] == 1 and money[1] == 1:
        return 1
    elif money[0] == 1 and money[1] == 0:
        return 2
    elif money[0] == 0 and money[1] == 0:
        return 3
    elif money[0] == 0 and money[1] == 1:
        return 4


def borders(): #определение двух точек для построения бортов
    point1 = [(180, 180), (180, 284), (284, 180), (284, 284)]
    point2 = [(640, 640), (540, 640), (640, 540), (540, 540)]
    point1_rec = random.choice(point1)
    point2_rec = random.choice(point2)
    canvas.create_rectangle(point1_rec, point2_rec, fill=None, width=5)
    return point1_rec, point2_rec


def robot_position(): #расчет позиции робота
    point1, point2 = borders()
    x1rect = point1[0]
    y1rect = point1[1]
    x2rect = point2[0]
    y2rect = point2[1]
    start = start_zone()
    direction = coins()
    a = kubik()
    if start == 1 or start == 3:
        if start == 1:
            angle = 180 if direction == 1 else 0
            x = 300 if a == 1 or a == 2 or a == 3 else 420
            y = 200 if a == 1 or a == 4 else 130 if a == 2 or a == 5 else 50
        if start == 3:
            angle = 0 if direction == 1 else 180
            x = 420 if a == 1 or a == 2 or a == 3 else 300
            y = 560 if a == 1 or a == 4 else 640 if a == 2 or a == 5 else 700
        if x1rect < x and y1rect < y and x2rect > x and y2rect > y:
            while x1rect < x and y1rect < y and x2rect > x and y2rect > y:
                a = kubik()
                if start == 1:
                    angle = 180 if direction == 1 else 0
                    x = 300 if a == 1 or a == 2 or a == 3 else 420
                    y = 200 if a == 1 or a == 4 else 130 if a == 2 or a == 5 else 50
                if start == 3:
                    angle = 0 if direction == 1 else 180
                    x = 420 if a == 1 or a == 2 or a == 3 else 300
                    y = 560 if a == 1 or a == 4 else 640 if a == 2 or a == 5 else 700
    if start == 2 or start == 4:
        if start == 2:
            angle = 180 if direction == 1 else 0
            x = 560 if a == 1 or a == 4 else 640 if a == 2 or a == 5 else 700
            y = 300 if a == 1 or a == 2 or a == 3 else 420
        if start == 4:
            angle = 0 if direction == 1 else 180
            x = 200 if a == 1 or a == 4 else 130 if a == 2 or a == 5 else 50
            y = 420 if a == 1 or a == 2 or a == 3 else 300
        if x1rect < x and y1rect < y and x2rect > x and y2rect > y:
            while x1rect < x and y1rect < y and x2rect > x and y2rect > y:
                if start == 2:
                    angle = 180 if direction == 1 else 0
                    x = 560 if a == 1 or a == 4 else 640 if a == 2 or a == 5 else 700
                    y = 300 if a == 1 or a == 2 or a == 3 else 420
                if start == 4:
                    angle = 0 if direction == 1 else 180
                    x = 200 if a == 1 or a == 4 else 130 if a == 2 or a == 5 else 50
                    y = 420 if a == 1 or a == 2 or a == 3 else 300
    return x, y, start, angle


tk = Tk()
tk.resizable(0, 0)
canvas = Canvas(tk, bg='white', height=1200, width=950, bd=0, highlightthickness=0)
canvas.pack()
test = PhotoImage(file='resources/pole.gif')
testImg = canvas.create_image(0, 0, anchor=NW, image=test)

btn_gen = Button(tk, text='New generation', width=15, height=1, bd='3', command=restart_program)
btn_ex = Button(tk, text='Exit', width=15, height=1, bd='3', command=tk.destroy)


btn_gen.place(x=825, y=50)
btn_ex.place(x=825, y=100)



x, y, st, an = robot_position()
car13 = Image.open("resources/car13.gif")
car24 = Image.open("resources/car24.gif")
angle = an

if st == 1 or st == 3:
    out = car13.rotate(angle, expand=True)
    out.save('car13.gif')
    car13 = PhotoImage(file="resources/car13.gif")
    canvas.create_image(x, y, anchor=NW, image=car13)

if st == 2 or st == 4:
    out = car24.rotate(angle, expand=True)
    out.save('car24.gif')
    car24 = PhotoImage(file="resources/car24.gif")
    canvas.create_image(x, y, anchor=NW, image=car24)
tk.mainloop()
