import tkinter as tk
from datetime import datetime, timedelta

# Initialize the main window
root = tk.Tk()
root.title("Stopwatch")
root.geometry("250x150")

# Variables to keep track of time
start_time = None
elapsed_time = timedelta(0)
running = False

# Update the timer display
def update_timer():
    if running:
        current_time = datetime.now()
        delta = current_time - start_time + elapsed_time
        timer_label.config(text=str(delta).split(".")[0])  # Display up to seconds only
        root.after(100, update_timer)

# Start the stopwatch
def start():
    global running, start_time
    if not running:
        start_time = datetime.now()
        running = True
        update_timer()

# Stop the stopwatch
def stop():
    global running, elapsed_time
    if running:
       
 if runnig stopwatch 