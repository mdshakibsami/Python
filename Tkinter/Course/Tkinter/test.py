from tkinter import *

root = Tk()
root.geometry("500x500")
#________________________________________________

#Entry
name = Entry(root)
name.pack()
roll = Entry(root)
roll.pack()
reg = Entry(root)
reg.pack()
#e = Entry(root).pack()  --> doesn't work like that

#function
def getText():
    n = name.get()
    ro= roll.get()
    re = reg.get()
    f = open("test.txt","a")
    f.write(f"[{n},{ro},{re}],")
    f.write("\n")
    f.close()
    name.delete(0,END)
    roll.delete(0,END)
    reg.delete(0,END)
#button 
w_button=Button(root,text="click",bg="green",command=getText).pack()

#________________________________________________
root.mainloop()