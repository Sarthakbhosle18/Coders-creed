from tkinter import *

win = Tk()
win.title("Calculator")
win.geometry("500x500")

# Calculator logic functions
def click(value):
    current = e1.get()
    e1.delete(0, END)
    e1.insert(0, str(current) + str(value))

def clear():
    e1.delete(0, END)

def evaluate():
    try:
        result = eval(e1.get())
        e1.delete(0, END)
        e1.insert(0, str(result))
    except:
        e1.delete(0, END)
        e1.insert(0, "Error")

form = LabelFrame(win, padx=10, pady=10)
l1 = Label(form, text="Calculator")
l1.pack()

e1 = Entry(form, font=("comic sans ms", 20), justify=RIGHT)
e1.pack(pady=10)

# Frame to hold the calculator buttons
btn_frame = Frame(form)
btn_frame.pack()

# Row 1: Clear, Division, Multiplication, Subtraction
Button(btn_frame, text="C", width=5, height=2, font=("arial", 14), command=clear).grid(row=0, column=0, padx=5, pady=5)
Button(btn_frame, text="/", width=5, height=2, font=("arial", 14), command=lambda: click("/")).grid(row=0, column=1, padx=5, pady=5)
Button(btn_frame, text="*", width=5, height=2, font=("arial", 14), command=lambda: click("*")).grid(row=0, column=2, padx=5, pady=5)
Button(btn_frame, text="-", width=5, height=2, font=("arial", 14), command=lambda: click("-")).grid(row=0, column=3, padx=5, pady=5)

# Row 2: 7, 8, 9, Addition
Button(btn_frame, text="7", width=5, height=2, font=("arial", 14), command=lambda: click(7)).grid(row=1, column=0, padx=5, pady=5)
Button(btn_frame, text="8", width=5, height=2, font=("arial", 14), command=lambda: click(8)).grid(row=1, column=1, padx=5, pady=5)
Button(btn_frame, text="9", width=5, height=2, font=("arial", 14), command=lambda: click(9)).grid(row=1, column=2, padx=5, pady=5)
Button(btn_frame, text="+", width=5, height=2, font=("arial", 14), command=lambda: click("+")).grid(row=1, column=3, padx=5, pady=5)

# Row 3: 4, 5, 6
Button(btn_frame, text="4", width=5, height=2, font=("arial", 14), command=lambda: click(4)).grid(row=2, column=0, padx=5, pady=5)
Button(btn_frame, text="5", width=5, height=2, font=("arial", 14), command=lambda: click(5)).grid(row=2, column=1, padx=5, pady=5)
Button(btn_frame, text="6", width=5, height=2, font=("arial", 14), command=lambda: click(6)).grid(row=2, column=2, padx=5, pady=5)
Button(btn_frame, text="=", width=5, height=5, font=("arial", 14), command=evaluate).grid(row=2, column=3, rowspan=2, padx=5, pady=5)

# Row 4: 1, 2, 3
Button(btn_frame, text="1", width=5, height=2, font=("arial", 14), command=lambda: click(1)).grid(row=3, column=0, padx=5, pady=5)
Button(btn_frame, text="2", width=5, height=2, font=("arial", 14), command=lambda: click(2)).grid(row=3, column=1, padx=5, pady=5)
Button(btn_frame, text="3", width=5, height=2, font=("arial", 14), command=lambda: click(3)).grid(row=3, column=2, padx=5, pady=5)

# Row 5: 0, Decimal point
Button(btn_frame, text="0", width=12, height=2, font=("arial", 14), command=lambda: click(0)).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
Button(btn_frame, text=".", width=5, height=2, font=("arial", 14), command=lambda: click(".")).grid(row=4, column=2, padx=5, pady=5)

form.pack()

win.mainloop()
