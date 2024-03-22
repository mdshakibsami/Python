from tkinter import *

root = Tk()
#_______________________________________________

def clickBtn():
    new_label = Label(root,text="Button is clicked").pack()

disable_btn = Button(root, text="I'm disable",state=DISABLED,padx=10,pady=5).pack()
btn = Button(root, text="Click Me",command=clickBtn,fg="blue",bg="green").pack() # command =this function don't need ()

#_______________________________________________
root.mainloop()