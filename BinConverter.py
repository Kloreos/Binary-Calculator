#Disclaimer: Full project by PetesHacker, for personal use only

from tkinter import *
import tkinter as tk
window = tk.Tk()

window.title("Binary Calculator")
window.geometry('300x400')
window.configure(bg = '#BBD5EA')
window.resizable(False,False)
window.iconbitmap(default = 'icon.ico')

retry_msg = 'Error pls retry'
user = Entry(window,width = 50, border = 0)
user.place(x = 0,y = 0)


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
    
def commandt():
    user.insert(0,"1")
def command0():
    user.insert(0,"0")

bttn(0,100,10,14,"1",'#485866','#F0FAEF',commandt)
bttn(86,100,10,14,"0",'#485866','#F0FAEF',command0)
Button(window, width = 5, height = 1 ,text = "+")

testtype = user.get()

labelans = Label(window, width = 10, height = 1, text = '', foreground = '#262626')
labelans.place(x = 0, y = 16)

def clearend():
   user.delete(0, END)
   labelans.configure(text = '')


def check():
    testtype = user.get()
    try:
        conv = int(testtype,2)
        conv2 = float(conv)
        print("passed")
        labelans.configure(text = conv2)
        print(conv)
        
        

    except(ValueError):
        print(testtype)
        labelans.configure(text = retry_msg)
        print(retry_msg)
        
storelist = []

# def addition():
#     # try:
#     convert = int(user.get())
#     f = user.get()
#     storelist.append(f,0)
#     user.delete(0, END)
#     f2 = user.get()
#     storelist.append(f2,1)
#     sum = bin(int(f, 2) + int(f2, 2))
#     print(sum)
#     labelans.config(sum)
#     storelist.clear()
#     # except ValueError:
#     #     labelans.configure(text = retry_msg)
#     #     print(retry_msg)
    
bttn(200,100,7,1,"convert",'#485866','#F0FAEF',check)
bttn(200,50,7,1,"Clear",'#485866','#F0FAEF',clearend)
# bttn(200,200, 7, 1, "Addition",'#485866','#F0FAEF',addition)



window.mainloop()