import tkinter as tk
from tkinter.constants import X
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle

# ---------------------------------------------------------------------------------
root = tk.Tk()
style = ThemedStyle(root)

root.wm_resizable(False, False)

style.set_theme("adapta")
root.geometry("350x250")

root.iconbitmap("icon.ico")

root.title("Calculator")
# Entry Widgets to show calculations
Display = tk.Entry(root, font="B 20")
Display.pack(fill=X)


def nine():
    Display.insert("end", "9")


def eight():
    Display.insert("end", "8")


def seven():
    Display.insert("end", "7")


def six():
    Display.insert("end", "6")


def five():
    Display.insert("end", "5")


def four():
    Display.insert("end", "4")


def three():
    Display.insert("end", "3")


def two():
    Display.insert("end", "2")


def one():
    Display.insert("end", "1")


def zero():
    Display.insert("end", "0")


def double_zero():
    Display.insert("end", "00")


def point():
    Display.insert("end", ".")


def plus():
    Display.insert("end", "+")


def minus():
    Display.insert("end", "-")


def mul():
    Display.insert("end", "*")


def divide():
    Display.insert("end", "/")


def modulus():
    Display.insert("end", "%")


def result():
    if Display.get() == "":
        Display.insert("end", "error")
    elif Display.get()[0] == "0":
        Display.delete(0, "end")
        Display.insert("end", "error")
    else:
        res = Display.get()
        res = eval(res)
        Display.insert("end", " = ")
        Display.insert("end", res)


def clear():
    Display.delete(0, "end")


btns_frame = tk.Frame(width=312, height=272.5, bg="grey")

btns_frame.pack()

# first row

clear = ttk.Button(btns_frame, text="C", command=clear, width=40).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = ttk.Button(btns_frame, text="÷", command=divide).grid(row=0, column=3, padx=1, pady=1)

# second row

seven = ttk.Button(btns_frame, text="7", command=seven).grid(row=1, column=0, padx=1, pady=1)

eight = ttk.Button(btns_frame, text="8", command=eight).grid(row=1, column=1, padx=1, pady=1)

nine = ttk.Button(btns_frame, text="9", command=nine).grid(row=1, column=2, padx=1, pady=1)

multiply = ttk.Button(btns_frame, text="x", command=mul).grid(row=1, column=3, padx=1, pady=1)

# third row

four = ttk.Button(btns_frame, text="4", command=four).grid(row=2, column=0, padx=1, pady=1)

five = ttk.Button(btns_frame, text="5", command=five).grid(row=2, column=1, padx=1, pady=1)

six = ttk.Button(btns_frame, text="6", command=six).grid(row=2, column=2, padx=1, pady=1)

minus = ttk.Button(btns_frame, text="-", command=minus).grid(row=2, column=3, padx=1, pady=1)

# Forth Row

one = ttk.Button(btns_frame, text="1", command=one).grid(row=3, column=0, padx=1, pady=1)

two = ttk.Button(btns_frame, text="2", command=two).grid(row=3, column=1, padx=1, pady=1)

three = ttk.Button(btns_frame, text="3", command=three).grid(row=3, column=2, padx=1, pady=1)

plus = ttk.Button(btns_frame, text="+", command=plus).grid(row=3, column=3, padx=1, pady=1)

# last row

equals = ttk.Button(btns_frame, text="=", command=result, width=25).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = ttk.Button(btns_frame, text=".", command=point).grid(row=4, column=3, padx=1, pady=1)

zero = ttk.Button(btns_frame, text="0", command=zero).grid(row=4, column=2, padx=1, pady=1)

root.mainloop()
