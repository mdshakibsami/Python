#-------------------------------------------- import modules ---------------------------------
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import sqlite3
import pygame

from tkinter import simpledialog

from PIL import Image, ImageTk 

from twilio.rest import Client
#_____________________________________________________________________________________________________________________________


#--------------------------- Date and Time list ------------------------------
dates = []
times =[]

#--------------------------- Create Interface ------------------------------
root = Tk()
root.geometry("1500x800")
root.minsize(600,750)
root.title("Plan Your Day")
root.configure(bg="green")
root.resizable(True,True)
#icon
icon_img = PhotoImage(file="C:/Users/MD Shakib/Music/Plan Your Day Project/icons/task.png")
root.iconphoto(False,icon_img)
#----------------------------------------- heading text frame --------------------------------------------------------
up_frame = Frame(root,bg="#32405b",width=1200,height=60)
up_frame.pack(pady=10)
heading = Label(up_frame,text="Plan Your Day",font="arial 25 bold",bd=5,fg="#fff",background="#32405b",anchor=CENTER)
heading.grid(pady=20,padx=210,column=0,row=0)
#image
task_image_path = "C:/Users/MD Shakib/Desktop/Android/icons/task.png"
task_original_image = Image.open(task_image_path)
task_resized_image = task_original_image.resize((60, 60))
task_image = ImageTk.PhotoImage(task_resized_image)
Label(up_frame,image=task_image,bg="#32405b").place(x=150,y=15)

#____________________________________________________________________________________________________________________

#************************************************ Style ***************************************************************
#style variable
style = ttk.Style()
# #pick a theme
style.theme_use('default')
#configure the treeview color
style.configure('Treeview',
                background = "#EAEDED",
                foreground = "black",
                rowheight = 25,
                font = "arial 10 bold  ",
                fieldbackground = "#d3d3d3",
                
                )
# Configure style options for the Treeview headings
style.configure("Treeview.Heading",
                    background="#32405b",  # Heading background color
                    foreground="white",  # Heading text color
                    font = "arial 20 italic",
                    relief="flat" 
                    )
# Create a style for the heading on hover
style.map("Treeview.Heading",
          background = [('active',"green")])

#selected color
style.map("Treeview",
          background = [("selected","green")])

#_______________________________________________________________________________________________________________________


#************************************************** Database *******************************************************************

#connect to database
conn = sqlite3.connect('test.db')

#create a cursor instance
c = conn.cursor()

#create a table
c.execute("""CREATE TABLE if not exists test_table(
          Task text,
          Date TEXT,
          Time TEXT,
          Status text

          )""")

#commit changes
conn.commit()

#close our connection
conn.close()



#-------------------------------------- Function to Show data from database ------------------------------------
def query_db():
    #connect to database
    conn = sqlite3.connect('test.db')

    c = conn.cursor()
    #grab data from databsee
    c.execute("SELECT rowid,* FROM test_table ")
    records = c.fetchall()


    # Clear the Treeview
    my_tree.delete(*my_tree.get_children())
    #show data in treeView
    global count
    count = 1
    for record in records:
        if count%2==0:
            my_tree.insert(parent='',index=END,text="",iid=count,values=(count,record[1],record[2],record[3],record[0],record[4]),tags=("evenrow",))
        else:
            my_tree.insert(parent='',index=END,text="",iid=count,values=(count,record[1],record[2],record[3],record[0],record[4]),tags=("oddrow",))
        count+=1

    #commit changes
    conn.commit()
    conn.close()

#________________________________________________________________________________________________________________________________________________________________




#******************************************************* Treeview ************************************************************************
# #create treeview 
tree_frame = Frame(root,width=600,height=300)
tree_frame.pack(expand=True,fill=BOTH)

#------------------------- Scrollbar ---------------------------
#create a scrollbar 
tree_scrollbaar = Scrollbar(tree_frame)
tree_scrollbaar.pack(side=RIGHT,fill=Y)
#create treeview
my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scrollbaar.set,selectmode="extended")
my_tree.pack(expand=True,padx=5,pady=10,fill=BOTH)
#configure the scrollbar
tree_scrollbaar.config(command = my_tree.yview)
#Create stripe row tags
my_tree.tag_configure("evenrow",background="white")
my_tree.tag_configure("oddrow",background="lightblue")
#___________________________________________
#defining columns --> creat a space for column
my_tree["columns"]=("No.","Task","Date","Time","Id","Status")
my_tree.config(displaycolumns=("No.","Task","Date","Time","Status"))
#creating columns
my_tree.column("#0",width=0,stretch=0)
my_tree.column("No.",anchor=CENTER,width=30,minwidth=20)
my_tree.column("Task",anchor=W,width=200,minwidth=100)
my_tree.column("Date",anchor=CENTER,width=100,minwidth=80)
my_tree.column("Time",anchor=CENTER,width=100,minwidth=80)
my_tree.column("Id",anchor=CENTER,width=30,minwidth=30)
my_tree.column("Status",anchor=CENTER,width=100,minwidth=80)
#heading 
my_tree.heading("No.",text="No.",anchor=CENTER)
my_tree.heading("Task",text="Task",anchor=CENTER)
my_tree.heading("Date",text="Date",anchor=CENTER)
my_tree.heading("Time",text="Time",anchor=CENTER)
my_tree.heading("Id",text="ID",anchor=CENTER)
my_tree.heading("Status",text="Status",anchor=CENTER)

##_____________________________________________________________________________________________

#------------------------ Button frame --------------------
b_frame = Frame(root,height=300)
b_frame.pack(pady=5,fill=BOTH)

#label and edittext
task_label = Label(b_frame,text="Task: ",font="arial 12 bold")
date_label = Label(b_frame,text="Date: ",font="arial 12 bold")
time_label = Label(b_frame,text="Time: ",font="arial 12 bold")
task_label.grid(pady=5,padx=30,row=0,column=0)
date_label.grid(pady=5,padx=30,row=0,column=1)
time_label.grid(pady=5,padx=30,row=0,column=2)


task_entry = Entry(b_frame,width=12,font = "arial 15",bd=2)
date_entry = Entry(b_frame,width=12,font = "arial 15 italic",bd=2)
time_entry = Entry(b_frame,width=10,font = "arial 15 italic",bd=2)
task_entry.grid(padx=30,row=1,column=0)
date_entry.grid(padx=30,row=1,column=1)
time_entry.grid(padx=30,row=1,column=2)
#________________________________________________________________________________________________________________________





#******************************************** All Functions *****************************************************

#It creats two lists: times and dates by grabing data from database
def list_time_date():
    times.clear()
    dates.clear()
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    
    c.execute("SELECT rowid,* FROM test_table ")
    records = c.fetchall()
    
    
    for record in records:
        dates.append(record[2])
        times.append(record[3])
    
    conn.commit()
    conn.close()
list_time_date()

#It sets current date and time  on entry box 
def set_current_date_time():
    currnt_date_time = datetime.now()
    formated_date = currnt_date_time.strftime("%d/%m/%y")
    formated_time = currnt_date_time.strftime("%H:%M")
    date_entry.insert(0,formated_date)
    time_entry.insert(0,formated_time)
set_current_date_time()


#It clears entry boxes
def clear_box():
    task_entry.delete(0,END)
    date_entry.delete(0,END)
    time_entry.delete(0,END)
    

#+++++++++++++++++++++++++++++++++ Date and Time Validation Function ++++++++++++++++++++++++++++++++++++++++++

def date_time_validation():
    date_time_valid_flag = True
    date_time = datetime.now()
    
    task=task_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    
    if len(date)==8 and len(time) ==5 and task!="":
    
        demo_day = date[0]+date[1]
        demo_month = date[3]+date[4]
        
        demo_year = date[6]+date[7]
        demo_year = int(demo_year)
        
        demo_day_list =[]
        demo_month_list=[]
        
        
        def which_month():
            if int(demo_month) in [1,2,3,4,5,6,7,8,9,10,11,12]:
                if int(demo_month)==1:
                    days_in_month =31
                    return days_in_month
                elif int(demo_month)==2:
                    if (demo_year % 4 == 0 and demo_year % 100 != 0) or (demo_year % 400 == 0):
                        days_in_month=29
                    else:
                        days_in_month=28
                    return days_in_month
                elif int(demo_month)==3:
                    days_in_month =31
                    return days_in_month
                elif int(demo_month)==4:
                    days_in_month =30
                    return days_in_month
                elif int(demo_month)==5:
                    days_in_month =31
                    return days_in_month
                elif int(demo_month)==6:
                    days_in_month =30
                    return days_in_month
                elif int(demo_month)==7:
                    days_in_month =31
                    return days_in_month
                elif int(demo_month)==8:
                    days_in_month =31
                    return days_in_month
                elif int(demo_month)==9:
                    days_in_month =30
                    return days_in_month
                elif int(demo_month)==10:
                    days_in_month =31
                    return days_in_month
                elif int(demo_month)==11:
                    days_in_month =30
                    return days_in_month
                elif int(demo_month)==12:
                    days_in_month =31
                    return days_in_month
            else:
                return -1
        
        day_range = which_month()+1
        print(day_range)
           
        
        
        for i in range(1,day_range):
            demo_day_list.append(i)
        for i in range(1,13):
            demo_month_list.append(i)
            
        demo_hour = time[0]+time[1]
        demo_minute = time[3]+time[4]
        demo_hour_list =[]
        demo_minute_list=[]
        for i in range(24):
            demo_hour_list.append(i)
        for i in range(60):
            demo_minute_list.append(i)
        
        
        def errorMessage():
            if int(demo_day) in demo_day_list and int(demo_month) in demo_month_list and date[2]=='/' and date[5]=='/' and  len(date)==8 and  task!="" and len(time)==5 and time[2]==":" and int(demo_hour) in demo_hour_list and int(demo_minute) in demo_minute_list:  
                if date_elements_list[2]<current_date_elements_list[2]:
                    return "The year is invalid"
                elif date_elements_list[1]<current_date_elements_list[1]:
                    return "The month is invalid"
                elif date_elements_list[0]<current_date_elements_list[0]:
                    return "The Day is invalid"
                elif time_elements_list[0]<current_time_elements_list[0]:
                    return "The hour is invalid"
                else:
                    return "The minute is invalid\n Time shoud be one minute ahead"
            else:
                if int(demo_month) not in demo_month_list:
                    return "Month is out of range (1-12)"
                elif int(demo_day) not in demo_day_list:
                    return f"Day is out of range.This month has {day_range-1} days"
                elif int(demo_hour) not in demo_hour_list:
                    return "Hour is out of range (0-24)"
                elif int(demo_minute) not in demo_minute_list:
                    return "Minute is out of range (1-59)"
                        
                    
        
        
        if int(demo_day) in demo_day_list and int(demo_month) in demo_month_list and date[2]=='/' and date[5]=='/' and  len(date)==8 and  task!="" and len(time)==5 and time[2]==":" and int(demo_hour) in demo_hour_list and int(demo_minute) in demo_minute_list:  
            date_elements_list = date.split("/")
            time_elements_list = time.split(":")
                
            current_time= date_time.strftime("%H:%M")
            current_date = date_time.strftime("%d/%m/%y")
            current_date_elements_list= current_date.split('/')
            current_time_elements_list = current_time.split(':')
            
            
            
            try:
                for i in date_elements_list:
                    int(i)
                for i in time_elements_list:
                    int(i)
                      
                if(date_elements_list[2]>current_date_elements_list[2]):
                    pass
                elif(date_elements_list[2]==current_date_elements_list[2] and date_elements_list[1]>current_date_elements_list[1]):
                    pass
                elif(date_elements_list[2]==current_date_elements_list[2] and date_elements_list[1]==current_date_elements_list[1] and date_elements_list[0]>current_date_elements_list[0]):
                    pass
                elif(date_elements_list[2]==current_date_elements_list[2] and date_elements_list[1]==current_date_elements_list[1] and date_elements_list[0]==current_date_elements_list[0]):
                    
                    if(time_elements_list[0]>current_time_elements_list[0]):
                        pass
                    elif(time_elements_list[1]>current_time_elements_list[1] and time_elements_list[0]==current_time_elements_list[0]):
                        pass
                    elif(time_elements_list[1]==current_time_elements_list[1] and time_elements_list[0]==current_time_elements_list[0]):
                        messagebox.showerror("Time Error",errorMessage())
                        date_time_valid_flag = False
                    else:
                        messagebox.showerror("Time Error",errorMessage())
                        date_time_valid_flag = False
                        
                else:
                    messagebox.showerror("Date Error",errorMessage())
                    date_time_valid_flag =False                        
            except Exception as e:
                messagebox.showerror("Format Error","'Date' input string only contains 'number' and '/'\n'Time' input string only contains 'number' and ':'\nor may the date you put in is invalid")
                date_time_valid_flag = False     
                print("Exception")                
        else:
            messagebox.showerror("Invalid info",errorMessage()) 
            date_time_valid_flag = False       
    else:
        messagebox.showerror("Format Error","'Date' length must be 8 like 11/01/24\nand 'Time' length must be 5 like 15:18\nand 'Task' can't be empty\nor may Your input day,month,hour and minute out of their range")
        date_time_valid_flag = False    
    
    return date_time_valid_flag
            
#____________________________________________________________________________________________________________________


  
#********************************************** Add Task Function- ******************************************************

def add_task():
    if date_time_validation():
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        #inserting values from user using treeview
        c.execute("insert into test_table values(:task,:date,:time,:status)",
                  {
                      'task':task_entry.get(),
                      'date':date_entry.get(),
                      'time':time_entry.get(),
                      'status':"Incomplete"
                  })
        
        conn.commit()
        conn.close()
        #load the data to the treeview screen from database
        query_db()
        #update list => dates and times
        list_time_date()
        #change update button text if it changed by any reason
        # edit_taskB.config(text="Edit Task",bg="green")
        #calling functions
        clear_box()
        set_current_date_time()
#_____________________________________________________________________________________________________________________________




#************************************************* Update Data Function *******************************************************************
def update_task():
    selected= my_tree.selection()
    print(selected)
    if selected:
        current_text = edit_taskB.cget("text").strip()
        if current_text == "Edit Task":
            #getting values from selected item of treeview
            todo_data = my_tree.item(selected,"values")
            clear_box()
            #show on entry boxes
            task_entry.insert(0,todo_data[1])
            date_entry.insert(0,todo_data[2])
            time_entry.insert(0,todo_data[3])
            edit_taskB.config(text="   Update",bg="green")
            
        elif current_text =="Update":
            response = messagebox.askyesno("Update?","Do you want to Update??")
            if response:
                if date_time_validation():
                    edit_taskB.config(text="Edit Task",bg="green")
                     #connect to database
                    conn = sqlite3.connect('test.db')

                    #create a cursor instance
                    c = conn.cursor()
                    #getting the oid from selected item
                    todo_data = my_tree.item(selected,"values")
                    selected_oid = todo_data[4]
                    c.execute("""UPDATE test_table SET
                                Task = :task,
                                Date = :date,
                                Time = :time,
                                Status = :status

                                WHERE oid=:id""",
                                {
                                'task':task_entry.get(),   
                                'date':date_entry.get(),   
                                'time':time_entry.get(), 
                                'status':'Incomplete',
                                'id':selected_oid
                                }
                                )
                        
                    #commit changes
                    conn.commit()
                    conn.close()
                    #Updat Screen
                    query_db()
                    list_time_date()
                    clear_box()
                    set_current_date_time()   
            else: 
                edit_taskB.config(text="Edit Task",bg="green")
                clear_box()
                set_current_date_time()            
    else:
        messagebox.showerror("not selected","NO Item is selected")
#_____________________________________________________________________________________________________________________________



#************************************************** Delete Function *********************************************************
def delete_task():
        selected= my_tree.selection()
        if selected:
            response = messagebox.askyesno("Delete?","Do you want to delete?")
            if response:
                #change button color and text
                edit_taskB.config(text="Edit Task",bg="green")
                #getting selected oid
                todo_data = my_tree.item(selected,"values")
                delete_item_oid= todo_data[4]
                
                
                #-------------------delete data from database------------------------
                
                conn = sqlite3.connect('test.db')

                #create a cursor instance
                c = conn.cursor()
                
                #delete command
                c.execute("DELETE FROM test_table WHERE oid = ?",(delete_item_oid,))

                #commit changes
                conn.commit()
                #close our connection
                conn.close()

                #update on screen
                query_db() 
                
                #update list => dates and times
                list_time_date()
        else:
            messagebox.showerror("not selected","NO Item is selected")

#_____________________________________________________________________________________________________________________________




#*********************************************** Search Function ****************************************************************________________________________________________________________________________________
def search_data():
    search_value = simpledialog.askstring("Input","Search Task")
    if search_value:
        search_value = "%"+search_value+"%"
        # Connect to the SQLite3 database
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()

        # Example: Searching for records with a specific condition
        cursor.execute("SELECT rowid,* FROM test_table WHERE Task like  ?", (search_value,))
        results = cursor.fetchall()

        if results:
            print(f"Records found with value '{search_value}':") 
        # Clear existing items in the Treeview
            my_tree.delete(*my_tree.get_children())
            count = 1
            for record in results:
                if count%2==0:
                    my_tree.insert(parent='',index=END,text="",iid=count,values=(count,record[1],record[2],record[3],record[0],record[4]),tags=("evenrow",))
                else:
                    my_tree.insert(parent='',index=END,text="",iid=count,values=(count,record[1],record[2],record[3],record[0],record[4]),tags=("oddrow",))
                count+=1
        else:
            messagebox.showerror("Not found",f"No task found with value {search_value}")

        # Close the database connection
        conn.close()

#_____________________________________________________________________________________________________________________________



#********************************************** Add phone Number function ************************************************
def add_number():
    number = simpledialog.askstring("Input","Enter your number")
    def number_flag():
        number_flag = True
        try:
            for i in range(1,len(number)):
                num=int(number[i])
                
            if(len(number)==14 and number[0]=='+'):
                pass
            else:
                number_flag =False
                messagebox.showerror("Invalid Number","INVALID NUMBER\nPlease Input valid Number country code '+880'")
              
        except Exception as e:
            number_flag = False
            messagebox.showerror("Invalid Number","INVALID NUMBER\nPlease Input valid Number with country code '+880'")
            print("Please Input valid Number with country code '+880'")
        
        return number_flag
    #__________________________
    if number_flag():
        #connect to database
        conn = sqlite3.connect('test.db')
        #create a cursor instance
        c = conn.cursor()
        
        #create a table
        c.execute("""CREATE TABLE if not exists number_table(
                Number text

                )""")
        #clear the database
        c.execute('DELETE  FROM number_table')
        
        c.execute('INSERT INTO number_table (Number) VALUES (?)', (number,))
        messagebox.showinfo("Successful","Number added successfully!")

        #commit changes
        conn.commit()

        #close our connection
        conn.close()
        
#_____________________________________________________________________________________________________________________________



#It checks if number exist in databse or no....
def is_number_exist():
    number_exist =False
    conn = sqlite3.connect('test.db')
        #create a cursor instance
    c = conn.cursor()
    c.execute("SELECT * FROM number_table ")
    records = c.fetchall()
    if records:
        number_exist=True
            
    conn.commit()
    conn.close()
    return number_exist


#It returns the user number if exist....
def user_number():
    try:
        conn = sqlite3.connect('test.db')
        #create a cursor instance
        c = conn.cursor()
        c.execute("SELECT * FROM number_table ")
        records = c.fetchone()
        u_number = records[0]
        
        print(f"this is the user number {u_number}")
                
        conn.commit()
        conn.close()
        return u_number
    except Exception as e:
        pass

#It shows home function 
def show_home():
    clear_box()
    query_db()
    set_current_date_time()
    
#________________________________________________________________________________________________________________________________________________________________




#*********************************************** Buttons ************************************************************************************


# Open an image file
search_image_path = "C:/Users/MD Shakib/Desktop/Android/icons/search.png"
home_image_path = "C:/Users/MD Shakib/Desktop/Android/icons/home.png"
phone_image_path = "C:/Users/MD Shakib/Desktop/Android/icons/phone.png"

add_image_path = "C:/Users/MD Shakib/Desktop/Android/icons/add.png"
edit_image_path = "C:/Users/MD Shakib/Desktop/Android/icons/edit.png"
delete_image_path = "C:/Users/MD Shakib/Desktop/Android/icons/delete.png"

search_original_image = Image.open(search_image_path)
home_original_image = Image.open(home_image_path)
phone_original_image = Image.open(phone_image_path)

add_original_image = Image.open(add_image_path)
edit_original_image = Image.open(edit_image_path)
delete_original_image = Image.open(delete_image_path)

# Resize the image if needed
search_resized_image = search_original_image.resize((20,20))
home_resized_image = home_original_image.resize((20, 20))
phone_resized_image = phone_original_image.resize((20, 20))


add_resized_image = add_original_image.resize((40,40))
edit_resized_image = edit_original_image.resize((40,40))
delete_resized_image = delete_original_image.resize((30,40))


# Convert the Image object to a Tkinter PhotoImage object
home_image = ImageTk.PhotoImage(home_resized_image)
search_image = ImageTk.PhotoImage(search_resized_image)
phone_image = ImageTk.PhotoImage(phone_resized_image)

add_image = ImageTk.PhotoImage(add_resized_image)
edit_image = ImageTk.PhotoImage(edit_resized_image)
delete_image = ImageTk.PhotoImage(delete_resized_image)

# Create a Button widget with the image
home_button = Button(root, text="Home",font="arial 10 bold",bg="#FF681E",padx=3,pady=3,fg="#fff",image=home_image, command=show_home, bd=0,compound=LEFT)
home_button.place(x=10,y=8)

search_button = Button(root, text="Search",padx=3,pady=3,font="arial 10 bold",bg="#D3212C",fg="#fff",image=search_image, command=search_data, bd=0,compound=LEFT)
search_button.place(x=10,y=42)

phone_button = Button(root, text="Add Number",font="arial 10 bold",padx=3,pady=3,bg="#D3212C",fg="#fff",image=phone_image, command=add_number, bd=0,compound=LEFT)
phone_button.place(x=10,y=75)


#Add,edit,delete buttons
add_taskB= Button(b_frame,text="  Add Task",font="arial 15 bold",width=10,bg="#32405b",fg="#fff",bd=0,command=add_task,image=add_image,compound=LEFT)
add_taskB.grid(pady=20,padx=10,row=2,column=0,sticky=EW)
edit_taskB= Button(b_frame,text="   Edit Task",font="arial 15 bold",width=10,bg="green",fg="#fff",bd=0,command=update_task,image=edit_image,compound=LEFT)
edit_taskB.grid(pady=20,padx=10,row=2,column=1,sticky=EW)
delete_taskB= Button(b_frame,text="Delete Task",font="arial 15 bold",width=10,bg="#9A031E",fg="#fff",bd=0,command=delete_task,image=delete_image,compound=LEFT)
delete_taskB.grid(pady=20,padx=10,row=2,column=2,sticky=EW)

#_____________________________________________________________________________________________________________________________



# def delete_done_task(time):
#     #connect to database
#     conn = sqlite3.connect('test.db')

#     #create a cursor instance
#     c = conn.cursor()

    
#     c.execute("delete from test_table where time=?",(time,))
#     #commit changes
#     conn.commit()

#     #close our connection 
#     conn.close()

#******************************** Some Important Functions *************************************************************
#It play song 
def playAlarmSound():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/MD Shakib/Downloads/Music/heiakim - loli selling ice cream.mp3")
    pygame.mixer.music.play()                

#************** Function shows time and check time if it's same or not *******************************
def show_time_and_alarm_Clock(): 
    time_date =datetime.now()
    current_time= time_date.strftime("%H:%M:%S")
    formated_check_time = time_date.strftime("%H:%M")
    current_date = time_date.strftime("%d/%m/%y")
    date_label = Label(up_frame,text="Date "+current_date,font="arial 12 bold",bg="#32405b",fg="#FF6C22")
    date_label.place(x=470,y=15)
    time_label = Label(up_frame,text="Time "+current_time,font="arial 12 bold",bg="#32405b",fg="white")
    time_label.place(x=470,y=50)
    
    #______________________________________
    # Connect to the SQLite3 database
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    # Example: Checking if a record with a specific condition exists

    c.execute("SELECT * FROM test_table WHERE Date = ? And Time=? And Status=?" , (current_date,formated_check_time,"Incomplete"))
    result = c.fetchone()

    if result:
        try:
            account_sid = 'ACa15776ca44b89fbe4a7368319ea72cbd'
            auth_token = '6cb00e54d90bcc553af1ec24217c19e0'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                    body='Hello, this is a test message from Twilio!,this is my trail message',
                    #from_='+15203574696',
                    #to=user_number()
                    
                )
            print(user_number())
            print(message.body)
        except Exception as e:
            print(e)
        
        
        playAlarmSound()
        current_task = result[0]
        call_after_second = (60- int(time_date.strftime("%S")))*1000
        stopYes = messagebox.askOk(f"{current_task}",f"Time to do {current_task} Task.\nDo you want to stop Alarm!!!!!! ? ")
        if stopYes:
            pygame.mixer.music.stop()
            mark_as_complete = messagebox.askyesno("Complete",f"Do you want to mark {current_task} task as complete??")
            if mark_as_complete: 
                c.execute("SELECT * FROM test_table WHERE Time=?" , (formated_check_time,))
                result = c.fetchone()
                updateKey = result[2]
                print(updateKey)
                c.execute("UPDATE test_table SET Status =? WHERE Time =?",('Complete',updateKey))
                
                conn.commit()
                conn.close()
                list_time_date()
                query_db()
                
                # #calling again cause i need until program runs
                root.after(call_after_second,show_time_and_alarm_Clock)
            else:
                #upadate the lists
                list_time_date()
                query_db()
                # #calling again
                root.after(call_after_second,show_time_and_alarm_Clock)
        else:
            root.after(call_after_second,show_time_and_alarm_Clock)
    else:
        #calling itself after 1 sec 
        root.after(1000,show_time_and_alarm_Clock)  
              
       

#____________________________________________________________________________________________________________________________________________


#------------------------ Show message if user number is not in database --------------------------------------------------

if bool(is_number_exist):
    print("yes")
    
else:
    messagebox.showerror("Error","Please add you number \nTo add your number click on phone icon")
#_______________________________________________________________________________________________________________________________________


show_time_and_alarm_Clock()
query_db()
#mainloop
root.mainloop()
############################################### THE END #########################################################################
