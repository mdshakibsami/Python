#1 import module
from tkinter import *
from tkinter import messagebox

#2 configure and create main window

root = Tk()
root.geometry('500x600+800+200')
root.title("TO-DO-LIST")
root.config(bg="#A6ACAF")
root.resizable(width=False,height=False)


#4 creat widgets (frame,listbox,scrollbar,entry,button)

frame = Frame(root)
frame.pack(padx=5,pady=20)

lb = Listbox(frame,width=30,height=15,font=('Times',18),bd=0,fg="#464646",highlightthickness=3,selectbackground="#F39C12",activestyle=NONE)
lb.pack(side=RIGHT,fill=BOTH)

#5 tasklist
TaskD={

}

#display function
def display(tdic):
    for key in tdic:
        lb.insert(END,f"{TaskD[key]}    {key}")

#6 Scrolebar
sb = Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#7 Entry
todo_task = Entry(root,font=("times 15"),width=30)

todo_task.pack(pady=5)

todo_time = Entry(root,font=("times 15"),width=30)

todo_time.pack(pady=5)

#9 add task function
def add():
    time = todo_time.get()
    task=todo_task.get()
    #12:59
    if len(time)==5 and time!='' and  task !='' and int(time[0]) in [0,1]and int(time[1]) in [0,1,2] and time[2]==':' and int(time[3]) in [0,1,2,3,4,5] and int(time[4]) in [0,1,2,3,4,5,6,7,8,9]:
        lb.delete(0,"end")
        TaskD.__setitem__(time,task)
        display(TaskD)
        todo_task.delete(0,END)
        todo_time.delete(0,END)
    #9:59
    elif len(time)==4 and time!=''and task !='' and int(time[0]) in [0,1,2,3,4,5,6,7,8,9] and time[1]==':'  and int(time[2]) in [0,1,2,3,4,5] and int(time[3]) in [0,1,2,3,4,5,6,7,8,9]:
        lb.delete(0,"end")
        TaskD.__setitem__(time,task)
        display(TaskD)
        todo_task.delete(0,END)
        todo_time.delete(0,END)
    #12:9
    elif len(time)==4 and time!='' and  task !='' and int(time[0]) in [0,1]and int(time[1]) in [0,1,2] and time[2]==':' and  int(time[3]) in [0,1,2,3,4,5,6,7,8,9]:
        lb.delete(0,"end")
        TaskD.__setitem__(time,task)
        display(TaskD)
        todo_task.delete(0,END)
        todo_time.delete(0,END)
    #9:9
    elif len(time)==3 and time!='' and  task !='' and int(time[0]) in [0,1,2,3,4,5,6,7,8,9] and time[1]==':' and int(time[2]) in [0,1,2,3,4,5,6,7,8,9]:
        lb.delete(0,"end")
        TaskD.__setitem__(time,task)
        display(TaskD)
        todo_task.delete(0,END)
        todo_time.delete(0,END)
    else:
        messagebox.showinfo("Input error","Task can't be empty \n and time format is like 23:59")
#10 delete task function
def delete_task():
    value = lb.curselection()
    if value:
        index = value[0]
        val = lb.get(index)
        print(val)
        list_key = val.split(' ')
        key = list_key[4]
        print(key)
        if key in TaskD:
            del TaskD[key]
            lb.delete(0,END)
            display(TaskD)
    
    

#8 button
button_frame = Frame(root)
button_frame.pack(pady=5)
add_button = Button(button_frame,text="ADD",command=add)
add_button.pack(fill=BOTH,side=LEFT,expand=True)
delete_button = Button(button_frame,text="DELETE",command=delete_task)
delete_button.pack(fill=BOTH,side=LEFT,expand=True)

#11 Alarm section
import datetime
import winsound
def update():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    up_key = str(hour)+":"+str(minute)
    if up_key in TaskD:
        winsound.Beep(500,1000)
        messagebox.showinfo("Task",f"Time to do {TaskD[up_key]}  task")
        del TaskD[up_key]
        update()
    else:
        print(up_key)
        root.after(1000,update)
        lb.delete(0,END)
        display(TaskD)

update()


#3 mainloop
root.mainloop()

