<<<<<<< HEAD
import tkinter
from tkinter import *

=======
#import
import tkinter
from tkinter import *

#main window
>>>>>>> main
root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

#icon
image_icon = PhotoImage(file="Tkinter/todolist/task.png")
root.iconphoto(False,image_icon)

#top bar 
top_bar = PhotoImage(file="Tkinter/todolist/topbar.png")
Label(root,image=top_bar).pack()

dock_image = PhotoImage(file="Tkinter/todolist/dock.png")
Label(root,image=dock_image,bg="#32405b").place(x=30,y=25)
 
note_image = PhotoImage(file="Tkinter/todolist/task.png")
Label(root,image=note_image,bg="#32405b").place(x=30,y=25)

heading = Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=20)

#main
frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task =StringVar()
task_entry = Entry(frame,width=18,font = "arial 20",bd=0)
task_entry.place(x=10,y=7)

button = Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0)
button.place(x=300,y=0)

#listbox

frame1 = Frame(root,width=400,height=300,bg="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1,font="arial 12",width=40,height=16,bg="#32405b",fg='white',cursor='hand2',selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill = BOTH,padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview )

#delete
delete_img = PhotoImage(file="Tkinter/todolist/delete.png")
Button(root,image=delete_img,bd=0).pack(side=BOTTOM,pady=13)



root.mainloop()