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
                pygame.mixer.music.load("alarm_sound.mp3")  # Replace with your sound file
                pygame.mixer.music.play()
                break
            time.sleep(1)
        
        messagebox.showinfo("Alarm", "Time to wake up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
