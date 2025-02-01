class BankAccount:
    def __init__(self, name):
        self._balance = 0 
        self.name = name 
    
    def deposit(self,amount) :
        self._balance += amount 

    def withdraw(self,amount) :
        self._balance -= amount 
    
    def get_balance(self) :
        return self._balance 
    
    def __str__(self):
        return f"Name : {self.name} and Balance : Hidden "

pratik = BankAccount("pratik")
pratik.deposit(100)
print(pratik)
print(pratik.get_balance()) # output = 100 
pratik.withdraw(50) # output = 50 
pratik.deposit(400) # output = 450 
pratik.withdraw(100) # output = 350
print(pratik.get_balance())