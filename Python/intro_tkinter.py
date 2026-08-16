from tkinter import *

win = Tk()
win.title("Dhoom Machale")
win.geometry("690x690+69+69")
win.minsize(69,69)
win.maxsize(1000,800)
win.resizable(True,False)

win.config(background="cyan", cursor="clock")


l1 = Label(win,text="hello world" , font=("comic sans MS",25,"bold underline"),fg="green",bg="black",border=10,relief="raised",padx=30,pady=25)
l1.pack()
win.mainloop()