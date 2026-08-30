from tkinter import*


win = Tk()

navbar = Menu(win)
fileMenu = Menu(navbar,tearoff=0)
fileMenu.add_command(label="open file",command='open_file')
fileMenu.add_command(label="close file",command='close_file')
fileMenu.add_command(label="open folder",command='open_folder')
fileMenu.add_separator()
fileMenu.add_command(label="exit",command=win.quit)

editMenu = Menu(navbar,tearoff=0)
editMenu.add_command(label="undo",command='undo')
editMenu.add_command(label="redo",command='redo')
editMenu.add_separator()
editMenu.add_command(label="cut",command='cut')
editMenu.add_command(label="copy",command='copy')
editMenu.add_command(label="paste",command='paste')

navbar.add_cascade(lable="file",menu=fileMenu)
navbar.add_cascade(label="edit",menu=editMenu)
win.config(menu=navbar)

win.mainloop()