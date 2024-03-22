import tkinter as tk
from tkinter import messagebox

def show_message_box():
    result = messagebox.askokcancel("Confirmation", "Do you want to proceed?")
    if result:
        print("User clicked OK")
    else:
        print("User clicked Cancel")

# Create the main window
root = tk.Tk()
root.title("MessageBox Example")

# Create a button to trigger the message box
button = tk.Button(root, text="Show MessageBox", command=show_message_box)
button.pack(padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()
