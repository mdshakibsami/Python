from tkinter import * #it imports everything from tkinter module

root = Tk()   #root widget

### There is two step ... 1) creating the thing 2) put them on the screen ###

#creating Label widget 
new_label = Label(root,text="I'm the dark ")
#putting Label widget on the screen
new_label.pack()

#always need infinty main loop
root.mainloop()

