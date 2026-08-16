from tkinter import *

win = Tk()
win.title("Calculator")
win.geometry("500x500")

form = LabelFrame(win, padx=10, pady=10)
l1 = Label(form, text=("calculator"))
l1.pack()
e1 = Entry(form, font=("comic sans ms", 20))
e1.pack()
form.pack()


win.mainloop()