import tkinter as tk
import winsound
from tkinter import messagebox
from datetime import datetime

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = {}
        
        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack()
        
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()
        
        self.due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
        self.due_date_label.pack()
        
        self.due_date_entry = tk.Entry(root)
        self.due_date_entry.pack()
        
        self.due_time_label = tk.Label(root, text="Due Time (HH:MM AM/PM):")
        self.due_time_label.pack()
        
        self.due_time_entry = tk.Entry(root)
        self.due_time_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()
        
        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        due_date = self.due_date_entry.get()
        due_time = self.due_time_entry.get()
        
        if task:
            if due_date:
                try:
                    due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
                except ValueError:
                    messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
                    return
            else:
                due_date = None
            
            if due_time:
                try:
                    due_time = datetime.strptime(due_time, '%I:%M %p').time()
                except ValueError:
                    messagebox.showerror("Error", "Invalid time format. Please use HH:MM AM/PM.")
                    return
            else:
                due_time = None
            
            self.tasks[task] = (due_date, due_time)
            self.task_listbox.insert(tk.END, self.format_task_text(task, due_date, due_time))
            self.task_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)
            self.due_time_entry.delete(0, tk.END)
    
    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        
        if selected_task_index:
            task_text = self.task_listbox.get(selected_task_index[0])
            task = task_text.split(" (")[0]
            
            del self.tasks[task]
            self.task_listbox.delete(selected_task_index)
    
    def format_task_text(self, task, due_date, due_time):
        formatted_text = task
        if due_date:
            formatted_text += f" (Due: {due_date.strftime('%Y-%m-%d')}"
        if due_time:
            formatted_text += f" at {due_time.strftime('%I:%M %p')}"
        formatted_text += ")"
        return formatted_text

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import threading
import pygame

class ToDoListApp:
    def __init__(self, root):
        # ... (previous code)
        
        self.alarm_label = tk.Label(root, text="Set Alarm Time (HH:MM AM/PM):")
        self.alarm_label.pack()

        self.alarm_entry = tk.Entry(root)
        self.alarm_entry.pack()

        self.set_alarm_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack()

        self.alarm_thread = None

    def set_alarm(self):
        alarm_time_str = self.alarm_entry.get()
        
        try:
            alarm_time = datetime.strptime(alarm_time_str, '%I:%M %p').time()
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please use HH:MM AM/PM.")
            return

        current_time = datetime.now().time()

        if alarm_time < current_time:
            messagebox.showerror("Error", "Alarm time must be in the future.")
            return
        
        if self.alarm_thread and self.alarm_thread.is_alive():
            self.alarm_thread.join()

        self.alarm_thread = threading.Thread(target=self.run_alarm, args=(alarm_time,))
        self.alarm_thread.start()

    def run_alarm(self, alarm_time):
        while True:
            current_time = datetime.now().time()
            if current_time >= alarm_time:
                pygame.init()
                x=winsound.Beep(500,1000)
                pygame.mixer.music.load(x)  # Replace with your sound file
                pygame.mixer.music.play()
                break
            time.sleep(1)
        
        messagebox.showinfo("Alarm", "Time to wake up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
