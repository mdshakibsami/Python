import tkinter as tk

root = tk.Tk()

name = tk.Label(root,text="Name: ").grid(row=0,column=0)
edit1= tk.Entry(root).grid(row=0,column=1)
password = tk.Label(root,text='Password: ').grid(row=1,column=0)
edit2= tk.Entry(root).grid(row=1,column=1)
submit = tk.Button(root,text="Submit").grid(row=3,column=0)


root.mainloop()