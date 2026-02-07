import os
TASK_FILE = 'tasks.txt'

def load_tasks():
    tasks = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE,'r',encoding='utf-8') as f:
            for line in f:
                text,status = line.strip().rsplit("||",1)
                tasks.append({"text":text,"done":status == "done"})
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE,'w',encoding='utf-8') as f:
        for task in tasks:
            status = "done" if task['done'] else "not_done"
            f.write(f"{task['text']} || {status}\n")
            
def display_tasks(tasks):
    if not tasks:
        print('No tasks found')
    else:
        for i,task in enumerate(tasks,1):
            checkbox = "✓" if task['done'] else " "
            print(f"{i}. [{checkbox}] {task['text']}")

    print()
    
def task_manager():
    tasks = load_tasks()
    while True:
        print("Task Manager")
        print("1. Add  Tasks")
        print("2. View Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option from (1-5): ").strip()
        
        match choice:
            case '1':
                text = input("Enter your task : ").strip()
                if text:
                    tasks.append({"text":text,"done":False})
                    save_tasks(tasks)
                    print("Task added successfully!")
                else:
                    print("Task cannot be empty!")
                    
                    
            case '2':
                display_tasks(tasks)
                
                
            case '3':
                display_tasks(tasks)
                try:
                    task_num = int(input("Enter task number to mark as done: "))
                    if 1 <= task_num <= len(tasks):
                        tasks[task_num - 1]['done'] = True
                        save_tasks(tasks)
                        print("Task marked as done!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
                    
            case '4':
                display_tasks(tasks)
                try:
                    task_num = int(input("Enter task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        del tasks[task_num - 1]
                        save_tasks(tasks)
                        print("Task deleted successfully!")
                    else:
                        print("Invalid task number.")       
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
                    
            case '5':
                print("Exiting Task Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please choose a number between 1 and 5.")

task_manager()
                    
            
            
