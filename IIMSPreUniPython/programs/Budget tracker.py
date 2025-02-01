"""
1.add and remove items and prices
2. calculate and display the items , prices , budget"""

items = []
prices = []
budget = 0
while True :
    ch = input("Do you want to add or remove items or view budget or end (a/r/b/e): ")
    if ch == "a" :
        while True : 
            f = input("Enter item(q to stop): ") 
            if f == "q" : 
                break
            p = input("Enter price: ")
            if p.isdigit()  and int(p) > 0 :
                items.append(f)
                prices.append(int(p))
            else :
                print("Invalid price(should be positive number)")

    elif ch == "r" :
        for count , item  in enumerate(items):
            print(f"{count +1 }.{item} = {prices[count]}")
        while True :
            try :
                r1 = int(input("Enter index to remove item (-1 to stop): ")) -1
                if r1 == -2 :
                    break
                items.pop(r1)  # when u have element use remove when u have index use pop
                prices.pop(r1)
            except Exception as e:
                print("Invalid input.")
                print(f"Error occured : {e}")
    elif ch == "v" :
        for count , item  in enumerate(items):
            print(f"{count+1}.{item} = {prices[count]}")
            budget += prices[count]
        print(f"Your budget for today is  ${budget}.")
    elif ch == "e" :
        quit()
    else :
        print("Invalid input.")