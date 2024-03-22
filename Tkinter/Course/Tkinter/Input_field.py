from tkinter import *

root = Tk()
#________________________________________________

#Entry
w_entry = Entry(root)

w_entry.insert(0,"Enter your name: ") #pre_set strings
w_entry.pack()
#e = Entry(root).pack()  --> doesn't work like that

#function
def getText():
    say_hello = "Hello! "+ w_entry.get()
    w_label = Label(root,text=say_hello)
    w_label.pack()
#button 
w_button=Button(root,text="click",bg="green",command=getText).pack()

#________________________________________________
root.mainloop()