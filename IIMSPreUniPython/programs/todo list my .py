
tasks = []
while True : 
    ch = input("Add task or show a/s : ")
    if ch == "a" :
        while True : 
            task = input("Task (q to stop): ")
            if task == "q" :
                break
            tasks.append(task)
    elif ch == "s" : 
        for i,j in enumerate(tasks) :
            print(j,i)
        ch2 = int(input("To complete a task input the tasks line: "))
        tasks.pop(ch2)


    
              


    



