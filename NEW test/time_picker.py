from tkinter import *

root = Tk()

import datetime
def update():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second =datetime.datetime.now().second
    new_lvl.config(text=f"{hour}:{minute}:{second}")
    new_lvl.after(1000,update)

new_lvl = Label(text="")
new_lvl.pack()

update()

root.mainloop()
