import os
import json

def validate_file():
    #Validate if the JSON file exists and if the format is correct
    if os.path.exists(filePath):
        try:
            with open(filePath, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    else:
        return []
    
def add_task(filePath):
    tasks = validate_file()
    task = input("Type the new task:")
    taskObj = {}
    taskObj["id"] = str(len(tasks) + 1)
    taskObj["task"] = task
    tasks.append(taskObj)
    with open(filePath, "w") as file:
        json.dump(tasks, file, indent=4)

def view_tasks(filePath):
    with open(filePath, "r") as file:
        tasks = file.read()
        tasksJSON = json.loads(tasks)

        if len(tasksJSON) == 0:
            print("No tasks to show! Please add a task!")
        else:
            print("ID" + "\t" + "Task")    
            for task in tasksJSON:
                print(task["id"] + "\t" + task["task"])

def edit_task(filePath):
    with open(filePath, "r") as file:
        tasks = file.read()
        tasksJSON = json.loads(tasks)
        print("ID" + "\t" + "Task")
        for task in tasksJSON:
            print(task["id"] + "\t" + task["task"])
        id = input("Type the task ID:")
        for task in tasksJSON:
            if task["id"] == id:
                newTask = input("Type the new task:")
                task["task"] = newTask
    with open(filePath, "w") as file:
        json.dump(tasksJSON, file, indent=4)

def delete_task(filePath):
    with open(filePath, "r") as file:
        tasks = file.read()
        tasksJSON = json.loads(tasks)
        print("ID" + "\t" + "Task")
        for task in tasksJSON:
            print(task["id"] + "\t" + task["task"])
        id = input("Type the task ID:")
        tasksJSON = [task for task in tasksJSON if task["id"] != id]
    with open(filePath, "w") as file:
        json.dump(tasksJSON, file, indent=4)

def clean_list(filePath):
    with open(filePath, "w") as file:
        json.dump([], file, indent=4)

filePath = "todoList.json"
while True:
    print("Menu")
    print("1. Add task.")
    print("2. View tasks.")
    print("3. Edit task.")
    print("4. Delete task.")
    print("5. Clean list.")
    print("6. Exit.")
    option = int(input("type an option:"))
    if option == 1:
        add_task(filePath)
    elif option == 2:
        view_tasks(filePath)
    elif option == 3:
        edit_task(filePath)
    elif option == 4:
        delete_task(filePath)
    elif option == 5:
        clean_list(filePath)
    elif option == 6:
        break