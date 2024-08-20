import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

def clear_tasks():
    if messagebox.askyesno("Confirm Clear", "Do you really want to clear all tasks?"):
        listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple To-Do List")

# Create a listbox to display tasks
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Create an entry box to add new tasks
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create buttons to add, delete, and clear tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack(pady=5)

# Run the application
root.mainloop()
