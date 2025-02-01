budget_log = {}

while True:
    print("\nBudget Log Menu:")
    print("1. Add an item")
    print("2. View items")
    print("3. Calculate total price")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        item = input("Enter the name of the item: ")
        if item in budget_log:
            print(f"{item} is already in the log. Updating the price.")
        price = float(input("Enter the price of the item: "))
        budget_log[item] = price
        print(f"{item} added/updated in the log.")
    elif choice == "2":
        if not budget_log:
            print("No items in the log.")
        else:
            print("\nItems in the budget log:")
            for item, price in budget_log.items():
                print(f"- {item}: Rs {price:.2f}")
    elif choice == "3":
        total = sum(budget_log.values())
        print(f"\nTotal price of all items: Rs {total:.2f}")
    elif choice == "4":
        print("Exiting the budget log. Goodbye!")
        break
    else:
        print("Invalid option. Please choose again.")
