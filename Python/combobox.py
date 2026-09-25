from tkinter import *
from tkinter import ttk

win = Tk()

def submitForm():
    print(cb.get())
    print(sb.get())
    print("form submitted")
    
cities = ['pune','mumbai','chennai']
cb=ttk.Combobox(win,values=cities)
cb.pack()

sb=ttk.Spinbox(win,from_=0,to=10)
sb.pack()

btn= Button(win,text="submit",command=submitForm)
btn.pack()
win.mainloop()