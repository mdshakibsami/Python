from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#---------------------------------------------------------------------------------------------
root = Tk()
root.title("Treeview")
root.geometry("600x600")
#--------------------------------------------------------------------------------------------
#creating tree
my_tree = ttk.Treeview(root)
#defining columns --> creat a space for column
my_tree['columns']=("Name","ID","Roll")
#creating columns -->attribute of the column & it's items
my_tree.column("#0",width=0,stretch=0) #for vanishing the default column
my_tree.column("Name",anchor=CENTER,width=150,minwidth=100)
my_tree.column("ID",anchor=CENTER,width=100,minwidth=80)
my_tree.column("Roll",anchor=CENTER,width=200,minwidth=100)
# columns headings --> heading and it's attribute
my_tree.heading("Name",text="Name",anchor=CENTER)
my_tree.heading("ID",text="ID",anchor=CENTER)
my_tree.heading("Roll",text="Roll",anchor=CENTER)
#Adding data
data = [
    ["Shakib","101","22102021"],
    ["Naruto","102","22102022"],
    ["Kira","103","22102023"],
    ["Luffy","104","22102024"],
    ["Sanji","105","22102025"],
    ["Zoro","106","22102026"]
]

global count
count = 0
for record in data:
    my_tree.insert(parent="",index=END,iid=count,text="",values=(record[0],record[1],record[2]))
    count+=1

#packing tree
my_tree.pack(pady=30)


#---------------------------------------------------------------
#input and button frame
inFrame = Frame(root,bg="#000")
inFrame.pack(pady=20)
#labels
nl = Label(inFrame,text="Name")
nl.grid(padx=25,row=0,column=0)
IDl = Label(inFrame,text="ID")
IDl.grid(padx=25,row=0,column=1)
rl = Label(inFrame,text="Roll")
rl.grid(padx=25,row=0,column=2)
#input box
name_box = Entry(inFrame)
name_box.grid(padx=25,row=1,column=0)
id_box = Entry(inFrame)
id_box.grid(padx=25,row=1,column=1)
roll_box = Entry(inFrame)
roll_box.grid(padx=25,row=1,column=2)


#buttons functions
def addItems():
    global count
    name = name_box.get()
    id = id_box.get()
    roll = roll_box.get()
    if id !="" and name !="" and roll !="":
        my_tree.insert(parent="",index=END,iid=count,text="",values=(name,id,roll))
        count +=1
        name_box.delete(0,END)
        id_box.delete(0,END)
        roll_box.delete(0,END)
    else:
        messagebox.showinfo("info","Please, fill every field")
        
def clear_all():
    x = my_tree.get_children()
    for record in x:
        data.clear()
        my_tree.delete(record)

def clear_selected():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

def clear_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)
#buttons
submitB = Button(root,text="Submit",command=addItems)
submitB.pack(pady=10)
#special buttons ferame
bframe = Frame(root)
bframe.pack(pady=20)
clearB = Button(bframe,text="Clear All",command=clear_all).grid(padx=20,row=0,column=0)
selected_mulB = Button(bframe,text="Clear Selected",command=clear_selected).grid(padx=20,row=0,column=1)
clearOneB = Button(bframe,text="Clear One",command=clear_one).grid(padx=20,row=0,column=2)



#______________________________________________________

#----------------------------------------------------------------------------------------------
root.mainloop()

