from tkinter import * 

win = Tk()
win.geometry("300x300")

def submit():
    print(e1.get(),e2.get())

isHidden = True
def togglePassword():
    global isHidden
    if isHidden:
        isHidden = False
        e2.config(show=DISABLED)
        btn2.config(text="Hide")
    else:
        isHidden = True
        e2.config(show="*")
        btn2.config(text="Show")

form = LabelFrame(win,text="Login Form",padx=10,pady=10)

l1 = Label(form,text="Username")
l1.pack()

e1 = Entry(form,font=("comic sans ms",20))
e1.pack()

l2 = Label(form,text="Password")
l2.pack()

e2 = Entry(form,show="*")
e2.pack()

btn = Button(form,text="Submit",command=submit)
btn.pack()

btn2 = Button(form,text="Show",command=togglePassword)
btn2.pack()

form.pack()

win.mainloop()