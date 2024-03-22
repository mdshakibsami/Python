import tkinter as tk
from tkinter import messagebox
import pickle

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Todo List")

        self.tasks = []
        self.load_tasks()

        self.task_entry = tk.Entry(root, width=40)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.complete_task)
        self.task_list = tk.Listbox(root, selectmode=tk.SINGLE, width=40)

        self.populate_task_list()

        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)
        self.remove_button.grid(row=1, column=0, padx=10, pady=10)
        self.complete_button.grid(row=1, column=1, padx=10, pady=10)
        self.task_list.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def populate_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task["name"] + (" [Completed]" if task["completed"] else ""))

    def add_task(self):
        task_name = self.task_entry.get()
        if task_name:
            self.tasks.append({"name": task_name, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.populate_task_list()
            self.save_tasks()

    def remove_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.populate_task_list()
            self.save_tasks()

    def complete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.tasks[selected_index[0]]["completed"] = True
            self.populate_task_list()
            self.save_tasks()

    def save_tasks(self):
        with open("tasks.pickle", "wb") as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open("tasks.pickle", "rb") as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            self.tasks = []

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
