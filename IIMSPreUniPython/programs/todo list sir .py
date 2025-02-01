
tasks = []

while True:
    print("""
    1. Add task
    2. View tasks
    3. Complete task
    4. Remove task
    5. End
    """)
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if tasks:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks found!")

    elif choice == "3":
        if tasks:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            
            task_num = int(input("Enter the task number to complete: "))
            if 1 <= task_num <= len(tasks):
                print(f"Task '{tasks.pop(task_num - 1)}' completed!")
            else:
                print("Invalid task number!")
            
        else:
            print("No tasks to complete!")

    elif choice == "4":
        if tasks:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                print(f"Task '{tasks.pop(task_num - 1)}' removed!")
            else:
                print("Invalid task number!")
            
            print("Please enter a valid number!")
        else:
            print("No tasks to remove!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option! Please choose a number between 1 and 5.")
