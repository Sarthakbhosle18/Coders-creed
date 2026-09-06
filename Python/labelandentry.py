from tkinter import *

win = Tk()

def submitForm():
    print(f"Username:{e1.get()} password:{e2.get()}")

l1 = Label(win,text ="Username")
l1.pack()

e1 = Entry(win)
e1.pack()

l2= Label(win,text="password")
l2.pack()

e2= Entry(win,show="*")
e2.pack()

btn= Button(win,text="submit",command=submitForm)
btn.pack()

win.mainloop()
