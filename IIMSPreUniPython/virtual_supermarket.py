""""
Create a virtual supermarket. For every article there is a price per artical and a quantity 
The customers fill their carts, one after the other. Check if enough goods are available 
Create a reciept for each customer
"""
class Market :
    def __init__(self):
        self.inventory = {
        "Rice": 10,
        "Jam": 5,
        "Bread": 8,
        "Butter": 20,
        "Mayo": 15,
        "Flour" : 20,
        "Soap" : 30,
        "Detergent" : 10, 
        "Lotion" : 15,
        "Battery" : 30,
        "Water" : 50,
        "Biscuit" : 40
        } 
        self.value = {
        "Rice": 1000,
        "Jam": 50,
        "Bread": 80,
        "Butter": 20,
        "Mayo": 50,
        "Flour" : 20,
        "Soap" : 15,
        "Detergent" : 100, 
        "Lotion" : 150,
        "Battery" : 15,
        "Water" : 50,
        "Biscuit" : 5     
        }  
        self.cart = {}
    
    def view_stock(self) :
        print("\nName : Price Stock")
        for idx , name  in enumerate(self.inventory):
            print(f"{idx+1}.{name} : {self.value[name]} {self.inventory[name]} ")
    
    def add_to_cart(self) :
        while True :
            ch = input("Enter the item's name (q to stop adding):").capitalize() 
            if ch.lower() == "q" :
                break
            if ch not in self.inventory :
                print("We do not have that in stock.")
                continue
            
            quantity = input(f"Enter the number of {ch} :")
            
            if not quantity.isdigit() :
                print("Invalid Input.")
                continue
            quantity = int(quantity)
                
            if quantity > self.inventory[ch] :
                print(f"Available stock = {self.inventory[ch]}.Enter a valid quantity.")
                continue
            if ch in self.cart :
                self.cart[ch] += quantity
            else:
                self.cart[ch] =quantity
            self.inventory[ch] -= quantity
        
    
    def view_cart(self) :
        if not self.cart:
            print("Your cart is empty.")
            return
        print("Item : Price Quantity")
        total = 0
        for idx , item  in enumerate(self.cart) :
            print(f"{idx+1}.{item}: {self.value[item]} {self.cart[item]} ")
            total += self.value[item] * self.cart[item]
        print(f"Your total is Rs{total}.")
    
    def remove_item(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        while True :
            ch = input("Enter the item's name (q to stop removing / c to clear cart):").capitalize().strip()
            if ch.lower() == "q" :
                break
            elif ch.lower() == "c" :
                confirm = input("Are you sure?(yes/no):").lower()
                if confirm == "yes" :
                    self.cart.clear()
                elif confirm == "no" :
                    continue
                return
            if ch not in self.cart : # only checks for the keys
                print("You don't have that in the cart.")
                continue
            
            quantity = input(f"Enter the number of {ch} to remove :")
            
            if not quantity.isdigit() :
                print("Invalid Input.")
                continue
            quantity = int(quantity)
                
            if quantity > self.cart[ch] :
                print(f"Stock in cart = {self.cart[ch]}.Enter a valid quantity.")
                continue
            if quantity == self.cart[ch] :
                self.cart.pop(ch)
            elif quantity < self.cart[ch]: 
                self.cart[ch] -= quantity
            self.inventory[ch] += quantity
        
    
    def checkout(self) :
        if not self.cart:
            print("Your cart is empty.")
            return
        total = 0
        print("Item : Price Quantity")
        for idx , item in enumerate(self.cart) :
            print(f"{idx+1}.{item}: {self.value[item]} {self.cart[item]} ")
            total += self.value[item] * self.cart[item]
        print(f"Your total is Rs{total}.")
        self.cart.clear()
    
    def run(self):
        print("\nWelcome to the Virtual Supermarket!")
        while True:
           
            print("\n1. View Stock")
            print("2. Add to Cart")
            print("3. View Cart")
            print("4. Remove item")
            print("5. Checkout")
            print("6. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.view_stock()
            elif choice == "2":
                self.view_stock()
                self.add_to_cart()
            elif choice == "3":
                self.view_cart()
            elif choice == "4":
                self.view_cart()
                self.remove_item()
            elif choice == "5":
                self.view_cart()
                confirm = input("Do you want to proceed to checkout? (yes/no): ").lower()
                if confirm == "yes":
                    self.checkout()
                    print("\nThank you for visiting the Virtual Supermarket! Goodbye!")
                else:
                    print("\nReturning to the main menu...")
            elif choice == "6":
                print("\nThank you for visiting the Virtual Supermarket! Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")


supermarket = Market()
supermarket.run()




        

