from tkinter import *
import time
import turtle
import threading
import math
from tkinter import messagebox
import subprocess as sp



# số rùa
global n
# dem so rua toi dich
global global_counter

def clicked():
    a = txtnhapdl.get()
    b = float(a)
    x = b/2
    c = b 
    k= b/(b*6)
    if b >= 0:
        t = turtle.Turtle()
        turtle.bgcolor("black")
        t.speed(0)
        start = time.time()
        while b > x-1:
            t.pencolor(crl[int((b/0.1)%4)])
            t.hideturtle()
            t.circle(b)
            b = b - k
            t.pencolor("black")
            t.forward(c)
            t.left(90)
            t.forward(c)
        end = time.time()
        txttimedl.insert(END,end-start)
        turtle.bye()

def draw_circle(radius, t):
    # vẽ hinh tròn
    t.circle(radius)
    # vào miền găng
    with threadLock:
        global_counter += 1     #khi rùa tới dích += 1
        if global_counter==n:   #nếu số rùa tới đích đủ thì dừng
            turtle.bye()
    pass


def clicked1():
    a = txtnhapdl.get()
    child = sp.Popen(["python","python3.py",a])
    exit_codes = child.wait()
    exit_codes=exit_codes/1000
    txt1.insert(END,exit_codes)

 
if __name__ == '__main__':

    threadLock = threading.Lock()
    window = Tk()
    
    window.title("AoDD")
    crl = ["blue","red","yellow","green"]
    window.geometry('400x200')

    lblbk = Label(window,text="Nhap duong kinh ").grid(column=0,row=0)
    txtnhapdl = Entry(window,width=10)
    txtnhapdl.grid(column=1, row=0)
    btn = Button(window, text="Ve duong tron ", command=clicked)
    btn.grid(column=1, row=1)
    lbltime = Label(window,text="Thoi gian xu ly").grid(column=0,row=2)
    txttimedl = Entry(window,width=20)
    txttimedl.grid(column=1, row=2)
    btn1 = Button(window, text="Ve duong tron da luong ", command=clicked1)
    btn1.grid(column=2, row=1)
    txt1 = Entry(window,width=20)
    txt1.grid(column=2, row=2)

    window.mainloop()


