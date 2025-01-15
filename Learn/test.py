tasks = ["Eat lunch","Study for 7+ hours","Clean dishes","import files"]
run = True
def show_tasks():
    if len(tasks) >0:
        for i in range(0,len(tasks)):
            print(f"{i}.{tasks[i]}")
    else:
        print("No tasks found.")

def add_tasks():
    task = input("Enter task:")
    tasks.append(task)
    print("Task added to list.")
    
def del_tasks():
    task = input("Enter task:")
    if task in tasks:
        tasks.remove(task)
    else:
        print("No such tasks in list") 

while run:
    cmd = input("Enter:")
    if cmd == "showTasks":
        show_tasks()
    elif cmd == "removeTasks":
        del_tasks()
    elif cmd == "addTasks":
        add_tasks()
        con = input("New Task? Y/N:")
        if con == "Y":
            add_tasks()
        else:
            pass
        
        
    
    
    elif cmd == "quit":
        run = False
    else:
        print("Error command.")
