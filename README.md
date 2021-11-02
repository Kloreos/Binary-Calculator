# Binary-Calculator
#Disclaimer: Full project by PetesHacker, for personal use only
import time
from tkinter import *
import tkinter as tk
window = tk.Tk()
import pyperclip

window.title("Binary Calculator")
window.geometry('300x400')
window.configure(bg = '#BBD5EA')
window.resizable(False,False)


retry_msg = 'Error pls retry'
user = Entry(window,width = 50, )
user.place(x = 0,y = 0)

user2 = Entry(window,width = 50,)
user2.place(x = 0,y = 30)


def bttn(x,y,text,bgcolor,fcolor, cmd):


    def on_leave(e):
        b1['background'] = fcolor
        b1['foreground'] = bgcolor

    def on_enter(e):
        b1['background'] = bgcolor
        b1['foreground'] = fcolor


        
        
    b1 = Button(window,width = 10, height = 10, text=text, fg = 'White', bg = bgcolor, border = 0
    , activeforeground=fcolor, activebackground=bgcolor,font = ('Typewriter_Condensed',13),command = cmd)
    # b1.place(x =0, y = 0)
    b1.bind("<Leave>",on_leave)

    b1.bind("<Enter>",on_enter)

    b1.place(x = x, y = y)

def bttn(x,y,width,height,text,bgcolor,fcolor, cmd):


    def on_leave(e):
        b1['background'] = fcolor
        b1['foreground'] = bgcolor

    def on_enter(e):
        b1['background'] = bgcolor
        b1['foreground'] = fcolor


        
        
    b1 = Button(window,width = width, height = height, text=text, fg = 'White', bg = bgcolor, border = 0
    , activeforeground=fcolor, activebackground=bgcolor,font = ('Typewriter_Condensed',13),command = cmd)
    # b1.place(x =0, y = 0)
    b1.bind("<Leave>",on_leave)

    b1.bind("<Enter>",on_enter)

    b1.place(x = x, y = y)

e = user
d = user2


def copyanswer():
    clip = labelans["text"]
    pyperclip.copy(clip)

changeb = Button(window, width = 10, height = 1 ,text = "copy", bg = '#485866', fg = 'white', border = 0, command = copyanswer)
changeb.place(x = 230,y = 240)

testtype = user.get()

labelans = Label(window, width = 15, height = 1, text = '', foreground = '#262626')
labelans.place(x = 0, y = 48)

def clearend():
   user.delete(0, END)
   user2.delete(0,END)
   labelans.configure(text = '')

def addition():
    try:
        FirstBinary = user.get()
        SecondBinary = user2.get()
        sum = bin(int(FirstBinary, 2) + int(SecondBinary, 2))
        labelans.configure(text = sum[2:])
    except ValueError:
        labelans.configure(text = retry_msg)
        print(retry_msg)

def subtract():
    try:
        FirstBinary = user.get()
        SecondBinary = user2.get()
        sub = bin(int(FirstBinary, 2) - int(SecondBinary, 2))
        labelans.configure(text = sub[2:])
    except ValueError:
        labelans.configure(text = retry_msg)
        print(retry_msg)

def multiply():
    try:
        FirstBinary = user.get()
        SecondBinary = user2.get()
        sub = bin(int(FirstBinary, 2) * int(SecondBinary, 2))
        labelans.configure(text = sub[2:])
    except ValueError:
        labelans.configure(text = retry_msg)
        print(retry_msg)

storelist = []




endb = Button(width = 7, height = 1,text = "Clear",bg = '#485866',command = clearend, foreground = 'white', border = 0).place(x = 200,y = 50)
bttn(0,200, 40, 1, "Addition",'#485866','#F0FAEF',addition)
bttn(0,160, 40, 1, "Subtraction",'#485866','#F0FAEF',subtract)
bttn(0,120, 40, 1, "Multiply",'#485866','#F0FAEF',multiply)


window.mainloop()
