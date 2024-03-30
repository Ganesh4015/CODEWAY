
import tkinter as tk
tasks=[]
def add_task():
    task=entry.get()
    tasks.append(task)
    entry.delete(0,tk.END)
    display_tasks()

def remove_task():
    task=entry.get()
    if task in tasks:
        tasks.remove(task)
        entry.delete(0,tk.END)
        display_tasks()

def update_task():
    old_task=entry.get()
    new_task=entry2.get()
    if old_task in tasks:
        index=tasks.index(old_task)
        tasks[index]=new_task

    entry.delete(0,tk.END)
    entry2.delete(0,tk.END)
    display_tasks()


def display_tasks():
    task_list.delete(0,tk.END)
    for task in tasks:
        task_list.insert(tk.END,task)


window=tk.Tk()
window.title('TODO LIST')

label=tk.Label(window,text="Task:")
label.grid(row=0,column=0,padx=12,pady=12)

entry=tk.Entry(window)
entry.grid(row=0,column=1,padx=12,pady=12)

label2=tk.Label(window,text="New Task:")
label2.grid(row=1,column=0,padx=12,pady=12)

entry2=tk.Entry(window)
entry2.grid(row=1,column=1,padx=12,pady=12)

add_button=tk.Button(window,text="Add Task",command=add_task)
add_button.grid(row=2,column=0,padx=12,pady=12)

remove_button=tk.Button(window,text="Remove Task",command=remove_task)
remove_button.grid(row=2,column=1,padx=12,pady=12)

update_button=tk.Button(window,text="Update Task",command=update_task)
update_button.grid(row=2,column=2,padx=12,pady=12)

task_list=tk.Listbox(window)
task_list.grid(row=3,column=0,columnspan=3,padx=12,pady=10)
window.mainloop()
