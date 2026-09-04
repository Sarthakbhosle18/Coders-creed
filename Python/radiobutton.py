from tkinter import *

win = Tk()

def submitform():
    print(gender.get(),chk1.get())

l1= Label(win,text="gender")
l1.pack()
gender = StringVar()
r1 = Radiobutton(win, text= "male", value="male",variable=gender)
r1.pack()

r2 = Radiobutton(win, text= "female", value="female",variable=gender)
r2.pack()

r1.select()
r2.select()

chk1 =StringVar()
r3 = Checkbutton(win, text="Im agree with terms and condition",variable=chk1,onvalue="Agreed",offvalue="Disagreed")
r3.pack()

btn = Button(win,text= "submit",command=submitform)
btn.pack()
win.mainloop()