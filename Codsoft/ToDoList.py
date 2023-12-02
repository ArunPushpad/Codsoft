from tkinter import *
from tkinter import messagebox
root = Tk()

class ToDolist:
    def __init__(self,root):
        self.root = root
        self.root.title("ToDo List")

        self.tasks = []

        self.entry = Entry(root, width=50)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        add = Button(root, text="Add Task", command=self.add_task)
        add.grid(row=1, column=0, padx=10, pady=10)

        self.listbox = Listbox(root, width=50, height=15)
        self.listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        remove = Button(root, text="Remove Task", command=self.remove_task)
        remove.grid(row=3, column=0, columnspan=2, pady=10)

    def add_task(self):
        t = self.entry.get()
        if t:
            self.tasks.append(t)
            self.update_task_List()
            self.entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    def remove_task(self):
        select_index  = self.listbox.curselection()
        if select_index:
            t_index = select_index[0]
            removed  = self.tasks.pop(t_index)
            messagebox.showinfo("Task Removed", f'Task "{removed}" removed.')
            self.update_task_List()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove. ")

    def update_task_List(self):
        self.listbox.delete(0, END)
        for t in self.tasks:
            self.listbox.insert(END, t)



app = ToDolist(root)
root.mainloop()