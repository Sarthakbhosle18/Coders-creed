from tkinter import *
from tkinter import messagebox
win = Tk()
 
def showMsg():
    messagebox.showinfo("Tkinter","This is some information")
    # messagebox.showwarning("TKinter","This is a warning")
    # messagebox.showerror("TKinter","This is some error")
    
btn = Button(win,text="click me",command=showMsg)
btn.pack()
win.mainloop()