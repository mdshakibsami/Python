import tkinter as tk

def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        key = listbox.get(selected_index[0])  # Get the selected item (assumed to be a dictionary key)
        value = my_dict[key]  # Retrieve the corresponding value from the dictionary
        label.config(text=f"Selected Key: {key}, Value: {value}")

# Create the main window
root = tk.Tk()
root.title("Get Dictionary Key Using Anchor")

# Create a dictionary
my_dict = {
    "apple": 5,
    "banana": 3,
    "cherry": 7,
}

# Create a list of dictionary keys
keys = list(my_dict.keys())

# Create a listbox to display the keys
listbox = tk.Listbox(root)
for key in keys:
    listbox.insert(tk.END, key)
listbox.pack()

# Bind a function to handle selection events
listbox.bind("<<ListboxSelect>>", on_select)

# Create a label to display the selected key and value
label = tk.Label(root, text="")
label.pack()

root.mainloop()
