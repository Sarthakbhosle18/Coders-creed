from tkinter import*

win = Tk()

fruits = ['apple','banana','mango','orange']

def selectrFruit():
    print(lb.selection_get())

lb = Listbox(win,selectmode='multiple')
for i in fruits:
    lb.insert(END,i)
lb.pack()

btn = Button(win,text="submit",command=selectrFruit)
btn.pack()

win.mainloop()