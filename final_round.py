import random
from tkinter import *
import sys
from PIL import Image
import os


tk = Tk()
canvas = Canvas(tk, width=1000, height=950, bd=0, highlightthickness=0)
canvas.pack()
pole = PhotoImage(file='resources/pole.gif')
canvas.create_image(0, 0, anchor=NW, image=pole)


def restart_program(): #новая генерация (перезагрузка)
    python = sys.executable
    os.execl(python, python, * sys.argv)


def coins():
    coin = random.choice(range(0, 10000)) % 2 == 0
    return coin


def kubik():
    return int(random.randint(1, 6))


def start_zone():
    money = coins(), coins()
    if money[0] == 1 and money[1] == 1:
        return 1
    elif money[0] == 1 and money[1] == 0:
        return 2
    elif money[0] == 0 and money[1] == 0:
        return 3
    elif money[0] == 0 and money[1] == 1:
        return 4


def rand_k():
    return random.sample(range(1, 11), 4)

directin = coins()

btn_gen = Button(tk, text='New generation', width=15, height=1, bd='3', command=restart_program)
btn_ex = Button(tk, text='Exit', width=15, height=1, bd='3', command=tk.destroy)


btn_gen.place(x=825, y=50)
btn_ex.place(x=825, y=100)


def kolon_pos():
    a = directin
    p = 0
    start = 0
    i = rand_k()
    while start != 4:
        if i[p] == 1 or i[p] == 2 or i[p] == 3:
            fill = "Green" if a == 1 else "Red"
            if i[p] == 1:
                x = 540 if start == 1 else 640 if start == 2 else 280 if start == 3 else 180
                y = 180 if start == 1 else 540 if start == 2 else 640 if start == 3 else 280
            if i[p] == 2:
                x = 410 if start == 1 or start == 3 else 640 if start == 2 else 180
                y = 180 if start == 1 else 640 if start == 3 else 410
            if i[p] == 3:
                x = 280 if start == 1 else 640 if start == 2 else 540 if start == 3 else 180
                y = 180 if start == 1 else 280 if start == 2 else 640 if start == 3 else 540
            canvas.create_rectangle(x, y, x + 10, y + 10, fill = fill)
        if i[p] == 5 or i[p] == 6 or i[p] == 7:
            fill = "Red" if a == 1 else "Green"
            if i[p] == 5:
                x = 540 if start == 1 else 690 if start == 2 else 280 if start == 3 else 130
                y = 130 if start == 1 else 540 if start == 2 else 690 if start == 3 else 280
            if i[p] == 6:
                x = 410 if start == 1 or start == 3 else 690 if start == 2 else 130
                y = 130 if start == 1 else 700 if start == 3 else 410
            if i[p] == 7:
                x = 280 if start == 1 else 690 if start == 2 else 540 if start == 3 else 130
                y = 130 if start == 1 else 280 if start == 2 else 690 if start == 3 else 540
            canvas.create_rectangle(x, y, x + 10, y + 10, fill=fill)
        if i[p] == 4 or i[p] == 8 or i[p] == 9 or i[p] == 10 or i[p] == 11:
            if i[p] == 4:
                x1 = 280 if start == 1 else 640 if start == 2 else 540 if start == 3 else 180
                y1 = 180 if start == 1 else 280 if start == 2 else 640 if start == 3 else 540
                x2 = 540 if start == 1 else 640 if start == 2 else 280 if start == 3 else 180
                y2 = 180 if start == 1 else 540 if start == 2 else 640 if start == 3 else 280
                if a == 1:
                    fill1 = "Green"
                    fill2 = "Green"
                else:
                    fill1 = "Red"
                    fill2 = "Red"
            if i[p] == 8:
                x1 = 280 if start == 1 else 690 if start == 2 else 540 if start == 3 else 130
                y1 = 130 if start == 1 else 280 if start == 2 else 690 if start == 3 else 540
                x2 = 540 if start == 1 else 690 if start == 2 else 280 if start == 3 else 130
                y2 = 130 if start == 1 else 540 if start == 2 else 690 if start == 3 else 280
                if a == 1:
                    fill1 = "Red"
                    fill2 = "Red"
                else:
                    fill1 = "Green"
                    fill2 = "Green"
            if i[p] == 9:
                x1 = 280 if start == 1 else 690 if start == 2 else 540 if start == 3 else 130
                y1 = 130 if start == 1 else 280 if start == 2 else 690 if start == 3 else 540
                x2 = 540 if start == 1 else 640 if start == 2 else 280 if start == 3 else 180
                y2 = 180 if start == 1 else 540 if start == 2 else 640 if start == 3 else 280
                if a == 1:
                    fill1 = "Red"
                    fill2 = "Green"
                else:
                    fill1 = "Green"
                    fill2 = "Red"
            if i[p] == 10:
                x1 = 280 if start == 1 else 640 if start == 2 else 540 if start == 3 else 180
                y1 = 180 if start == 1 else 280 if start == 2 else 640 if start == 3 else 540
                x2 = 540 if start == 1 else 690 if start == 2 else 280 if start == 3 else 130
                y2 = 130 if start == 1 else 540 if start == 2 else 690 if start == 3 else 280
                if a == 1:
                    fill1 = "Green"
                    fill2 = "Red"
                else:
                    fill1 = "Red"
                    fill2 = "Green"
            canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill=fill1)
            canvas.create_rectangle(x2, y2, x2 + 10, y2 + 10, fill=fill2)
        p += 1
        start += 1
    return a


def robot_position():
    start = start_zone()
    direction = directin
    a = kubik()
    if start == 1 or start == 3:
        if start == 1:
            #angle = 180 if direction == 1 else 0
            x = 300 if a == 1 or a == 2 or a == 3 else 420
            y = 200 if a == 1 or a == 4 else 130 if a == 2 or a == 5 else 50
        if start == 3:
            #angle = 0 if direction == 1 else 180
            x = 420 if a == 1 or a == 2 or a == 3 else 300
            y = 560 if a == 1 or a == 4 else 640 if a == 2 or a == 5 else 700
    if start == 2 or start == 4:
        if start == 2:
            #angle = 180 if direction == 1 else 0
            x = 560 if a == 1 or a == 4 else 640 if a == 2 or a == 5 else 700
            y = 300 if a == 1 or a == 2 or a == 3 else 420
        if start == 4:
            #angle = 0 if direction == 1 else 180
            x = 200 if a == 1 or a == 4 else 130 if a == 2 or a == 5 else 50
            y = 420 if a == 1 or a == 2 or a == 3 else 300
    return x, y, start


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


x, y, st = robot_position()

if st == 1 or st == 3:
    if st == 1:
        if directin == 1:
            car13_r = PhotoImage(file="resources/car13_r.gif")
            canvas.create_image(x, y, anchor=NW, image=car13_r)
        else:
            car13 = PhotoImage(file="resources/car13.gif")
            canvas.create_image(x, y, anchor=NW, image=car13)
    if st == 3:
        if directin == 1:
            car13 = PhotoImage(file="resources/car13.gif")
            canvas.create_image(x, y, anchor=NW, image=car13)
        else:
            car13_r = PhotoImage(file="resources/car13_r.gif")
            canvas.create_image(x, y, anchor=NW, image=car13_r)
if st == 2 or st == 4:
    if st == 2:
        if directin == 1:
            car24_r = PhotoImage(file="resources/car24_r.gif")
            canvas.create_image(x, y, anchor=NW, image=car24_r)
        else:
            car24 = PhotoImage(file="resources/car24.gif")
            canvas.create_image(x, y, anchor=NW, image=car24)
    if st == 4:
        if directin == 1:
            car24 = PhotoImage(file="resources/car24.gif")
            canvas.create_image(x, y, anchor=NW, image=car24)
        else:
            car24_r = PhotoImage(file="resources/car24_r.gif")
            canvas.create_image(x, y, anchor=NW, image=car24_r)
canvas.create_rectangle(284, 284, 540, 540, width=5)
kolon_pos()

tk.mainloop()

