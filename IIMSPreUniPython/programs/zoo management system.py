"""
welcome to virtual zoo 
1 add animal 
2 show animal 
3 calculate total food
4 exit
"""
class Animals:
    def __init__(self , name , age , food , food_req ):
        self.name = name
        self.age = age 
        self.food = food
        self.food_req = food_req

    def feed(self):
        print(f"{self.name} ate the food.")

while True :
    ch = input("Would you like to add or show animals or calculate toal food or end(a/s/c/e): ")
    if ch.lower() == "a" :
        name = input("Enter name : ")
        while True :
            age = input("Enter age : ")    
            if age.isdigit() :
                break
        food = input("Enter the type of food : ")
        while True :
            food_req = int(input("Enter the amt of food : " )) 
            if food_req.isdigit() :
                food_req = int(food_req)
                break


    
