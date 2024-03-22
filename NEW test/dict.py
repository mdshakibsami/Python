import tkinter as tk
from tkinter import ttk

def on_option_selected(event):
    selected_option = option_combobox.get()
    print(f"Selected option: {selected_option}")

# Create the main window
root = tk.Tk()
root.title("Option Picker")

# Create a list of options
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

# Create a Combobox for selecting the option
option_combobox = ttk.Combobox(root, values=options, state="readonly")
option_combobox.set("Select Option")  # Default text shown in the Combobox
option_combobox.grid(row=0, column=0, padx=10, pady=10)

# Bind the selection event to a function
option_combobox.bind("<<ComboboxSelected>>", on_option_selected)

# Run the Tkinter event loop
root.mainloop()
