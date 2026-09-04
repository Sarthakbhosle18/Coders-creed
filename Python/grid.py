import tkinter as tk
root = tk.Tk()
root.title("Grid")
label1= tk.Label(root,text="First Name:")
label1.grid(row=0,column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0,column=1)

label2 = tk.Label(root,text="Last Name:")
label2.grid(row=1,column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1,column=1)
root.mainloop()