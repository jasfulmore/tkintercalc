import tkinter as tk
import ast
from tkinter import font
import customtkinter

root = tk.Tk()
root.configure(bg="#2E2E2E")

button_font = ("Helvetica", 16)
button_bg = "#333333"
button_fg = "white"
button_bg_op = "#FF9500"
button_bg_misc = "#A6A6A6"


i = 0
def calculate(num):
    global i
    num1.insert(i, num)
    i += 1

def get_operation(operations):
    global i
    length = len(operations)
    num1.insert(i, operations)
    i += length


def clear_all():
    num1.delete(0, tk.END)



def equals():
    # extract all info present in entry or users provide
    entire_string = num1.get()
    # pass it to an AST module (import ast at top)
    try:
        node = ast.parse(entire_string, mode='eval')
    # takes the node and evaultes it and returns result
        result = eval(compile(node, '<string>', 'eval'))
    # clear all entries first before giving answer
        clear_all()
    # display results
        num1.insert(0, result)
    except Exception:
        clear_all()
        num1.insert(0, 'Err')


def undo():
    entire_string = num1.get()
    # makes sure theres chars in entry and deletes the last one and returns new string
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        num1.insert(0, new_string)
    else:
        clear_all()
        num1.insert(0, '')


root.title('Calculator')

num1 = tk.Entry(root, width=40, borderwidth=10, font=("Helvetica", 18, "bold"), bd=0, justify="right", bg="black", fg="white")
num1.grid(row=0, column=0, columnspan=7, padx=15, pady=15)

# creating buttons for caluclator
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = tk.Button(root, text=button_text, width=7, height=2, font=button_font, bg=button_bg, fg=button_fg, command=lambda text=button_text:calculate(num=text))
        button.grid(row=x+2, column=y, padx=2, pady=2)
        counter += 1

button = tk.Button(root, text='0', width=7, height=2, font=button_font, bg=button_bg, fg=button_fg, command=lambda: calculate(num='0'))
button.grid(row=5, column=1)

count = 0
operations = ['+', '-', '×', '÷', 'π', '%', '(', '^', ')', '^2']
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = tk.Button(root, text=operations[count], width=7, height=2, font=button_font, bg=button_bg, fg=button_fg, command=lambda text=operations[count]:get_operation(text))
            count += 1
            button.grid(row=x+2, column=y+3, padx=2, pady=2)

tk.Button(root, text='AC', width=7, height=2, font=button_font, bg=button_bg, fg=button_fg, command=clear_all).grid(row=5, column=0)
tk.Button(root, text='=', width=7, height=2, font=button_font, bg=button_bg, fg=button_fg, command=equals).grid(row=5, column=2)
tk.Button(root, text='<--', width=7, height=2, font=button_font, bg=button_bg, fg=button_fg, command= lambda :undo()).grid(row=5, column=4)


root.mainloop()