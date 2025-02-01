contacts = {}
while True : 
    ch = input("Add or show contacts (a/c): ")
    if ch == "a" :
        while True:
            name = input("Enter name (q to stop) : ")
            if name == "q" :
                break
            num = input("Enter number : ")
            contacts[name] = num
    elif ch == "c" : 
        print(contacts)
        

        


