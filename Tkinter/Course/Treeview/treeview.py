from tkinter import *
from tkinter import ttk
#---------------------------------------------------------------------------------------------
root = Tk()
root.title("Treeview")
root.geometry("500x500")
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
#insert take five arguments
'''
my_tree.insert(parent="",index=END,iid=0,text="",values=("Shakib","10827","22102021"))
my_tree.insert(parent="",index=END,iid=1,text="",values=("Shakib","10828","22102021"))
my_tree.insert(parent="",index=END,iid=2,text="",values=("Shakib","10829","22102021"))
my_tree.insert(parent="",index=END,iid=3,text="",values=("Shakib","10830","22102021"))
my_tree.insert(parent="",index=END,iid=4,text="",values=("Shakib","10822","22102021"))
'''
date = [
    ["Shakib","101","22102021"],
    ["Naruto","102","22102022"],
    ["Kira","103","22102023"],
    ["Luffy","104","22102024"],
    ["Sanji","105","22102025"],
    ["Zoro","106","22102026"]
]

count = 0
for record in date:
    my_tree.insert(parent="",index=END,iid=count,text="",values=(record[0],record[1],record[2]))
    count+=1

#packing tree
my_tree.pack()

#----------------------------------------------------------------------------------------------
root.mainloop()

