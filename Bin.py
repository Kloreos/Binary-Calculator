import tkinter as tk
import math


def clear_display(curr_input, curr_display):
	curr_input.delete(0, tk.END)
	curr_display.set('')
	return


def process_input(curr_input, curr_display):
	ans = math.ceil(eval(curr_input.get()))
	binary_ans = str('{0:b}'.format(ans))
	curr_display.set(binary_ans)
	return


def insert_btn_value(curr_input, numb):
	curr_input.insert(tk.END, numb)
	return


window = tk.Tk()

content = tk.Frame(master=window)
content.grid(row=0, column=0)

label = tk.Label(master=content, borderwidth=1, text='Binary Calculator')
label.grid(row=0, column=0, columnspan=4, pady=20)

###########
## operands
###########
frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=1)
frame.grid(row=1, column=0)
btn = tk.Button(master=frame, text='1', command=lambda: insert_btn_value(user_input, 1))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=1)
frame.grid(row=1, column=1)
btn = tk.Button(master=frame, text='2', command=lambda: insert_btn_value(user_input, 2))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=1)
frame.grid(row=1, column=2)
btn = tk.Button(master=frame, text='3', command=lambda: insert_btn_value(user_input, 3))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=1)
frame.grid(row=2, column=0)
btn = tk.Button(master=frame, text='4', command=lambda: insert_btn_value(user_input, 4))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=1)
frame.grid(row=2, column=1)
btn = tk.Button(master=frame, text='5', command=lambda: insert_btn_value(user_input, 5))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=1)
frame.grid(row=2, column=2)
btn = tk.Button(master=frame, text='6', command=lambda: insert_btn_value(user_input, 6))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=1)
frame.grid(row=3, column=0)
btn = tk.Button(master=frame, text='7', command=lambda: insert_btn_value(user_input, 7))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=1)
frame.grid(row=3, column=1)
btn = tk.Button(master=frame, text='8', command=lambda: insert_btn_value(user_input, 8))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=1)
frame.grid(row=3, column=2)
btn = tk.Button(master=frame, text='9', command=lambda: insert_btn_value(user_input, 9))
btn.pack()

frame = tk.Frame(master=content, relief=tk.RAISED, borderwidth=1)
frame.grid(row=4, column=1)
btn = tk.Button(master=frame, text='0', command=lambda: insert_btn_value(user_input, 0))
btn.pack()


############
## operators
############
frame = tk.Frame(master=content, borderwidth=1)
frame.grid(row=1, column=3)
btn = tk.Button(master=frame, text='+', command=lambda: insert_btn_value(user_input, '+'))
btn.pack()

frame = tk.Frame(master=content, borderwidth=1)
frame.grid(row=2, column=3)
btn = tk.Button(master=frame, text='-', command=lambda: insert_btn_value(user_input, '-'))
btn.pack()

frame = tk.Frame(master=content, borderwidth=1)
frame.grid(row=3, column=3)
btn = tk.Button(master=frame, text='*', command=lambda: insert_btn_value(user_input, '*'))
btn.pack()

frame = tk.Frame(master=content, borderwidth=1)
frame.grid(row=4, column=3)
btn = tk.Button(master=frame, text='/', command=lambda: insert_btn_value(user_input, '/'))
btn.pack()


frame = tk.Frame(master=content, borderwidth=1)
frame.grid(row=4, column=2)
btn = tk.Button(master=frame, text='=', command=lambda: process_input(user_input, user_display))
btn.pack()

frame = tk.Frame(master=content, borderwidth=1)
frame.grid(row=4, column=0)
btn = tk.Button(master=frame, text='X', command=lambda: clear_display(user_input, user_display))
btn.pack()


frame = tk.Frame(master=content)
frame.grid(row=5, column=0, columnspan=4)
user_input = tk.Entry(master=frame)
user_input.pack()

frame = tk.Frame(master=content)
frame.grid(row=6, column=0, columnspan=4)
user_display = tk.StringVar()
label = tk.Label(master=frame, textvariable=user_display)
label.pack()

window.mainloop()