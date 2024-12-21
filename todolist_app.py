import PySimpleGUI as sg

# Function to read tasks from the file
def read_file():
    ss = []
    try:
        with open("task.txt", "r") as reader:
            for line in reader:
                parts = line.strip("\n").split(",")
                if len(parts) == 2:
                    ss.append(parts)
    except FileNotFoundError:
        pass  # If file doesn't exist, start with an empty list
    return ss

# Function to write tasks to the file
def write_file(ss):
    with open("task.txt", "w") as writer:
        for x in ss:
            writer.write(f"{x[0]},{x[1]}\n")

# Function to add or save a task
def add_task(values):
    global is_edit_mode, edit_index
    priority = values['priority']
    taskname = values['taskname']

    if not priority or not taskname:
        sg.popup("Both Task Name and Priority are required!", title="Error")
        return

    if is_edit_mode:
        # Save edited task
        todolist[edit_index] = [priority, taskname]
        is_edit_mode = False
        window['add_save'].Update('Add')
    else:
        # Add new task
        todolist.append([priority, taskname])

    update_listbox()
    window['priority'].Update(value="")
    window['taskname'].Update(value="")

# Function to edit a selected task
def edit_task(values):
    global is_edit_mode, edit_index
    selected_task = values['todolist']
    if not selected_task:
        sg.popup("Please select a task to edit!", title="Error")
        return

    edit_index = todolist.index(selected_task[0])
    window['taskname'].Update(value=selected_task[0][1])
    window['priority'].Update(value=selected_task[0][0])
    is_edit_mode = True
    window['add_save'].Update('Save')

# Function to delete a selected task
def delete_task(values):
    selected_task = values['todolist']
    if not selected_task:
        sg.popup("Please select a task to delete!", title="Error")
        return

    todolist.remove(selected_task[0])
    update_listbox()

# Function to update the Listbox with current tasks
def update_listbox():
    window['todolist'].Update(values=todolist)

# Initialize variables
todolist = read_file()
is_edit_mode = False
edit_index = None

# Define the GUI layout
layout = [
    [sg.Text("Enter the task", font=("Arial", 14)), 
     sg.InputText("", font=("Arial", 14), size=(20, 1), key="taskname"),
     sg.Combo(['low', 'medium', 'high'], key="priority", font=("Arial", 14)),
     sg.Button("Add", font=("Arial", 14), key="add_save")],
    [sg.Listbox(values=todolist, size=(40, 10), font=("Arial", 14), key='todolist', enable_events=True)],
    [sg.Button("Edit", font=("Arial", 14)), sg.Button("Delete", font=("Arial", 14))]
]

# Create the Window
window = sg.Window("Task Manager", layout)

# Event Loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event == 'add_save':
        add_task(values)
    elif event == 'Edit':
        edit_task(values)
    elif event == 'Delete':
        delete_task(values)

# Save tasks to the file and close the window
write_file(todolist)
window.close()
