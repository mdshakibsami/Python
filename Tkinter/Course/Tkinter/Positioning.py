from tkinter import *

root = Tk()

#creating labels
new_label = Label(root,text="I'm the dark")
name_label = Label(root,text="Shakib")
#creating and setting on the screen
roll_label = Label(root,text="10202").grid(row=1,column=2) #python is oop,so you can grid when creating things
reg_label = Label(root,text="203").grid(row=1,column=6) # but it set on after roll_label cause grid is relational

#grid-->has columns and rows
new_label.grid(row=0,column=0) #default 
name_label.grid(row =1,column=1)

root.mainloop()