import tkinter as tk

root = tk.Tk()

redbutton = tk.Button(root,text="Red",fg='red')
redbutton.pack(side='left')

green_button = tk.Button(root,text='green',fg='green')
green_button.pack(side='right')

blue_button = tk.Button(root,text='Blue',fg='blue')
blue_button.pack(side='top')

black_button = tk.Button(root,text='Black',fg='black')
black_button.pack(side='bottom')

root.mainloop()