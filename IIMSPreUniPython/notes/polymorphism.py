# polymorphism = same method working in diffrent ways in diff senario.

x = "Hello world"
tuple = (1,2,3,4,5)
dict = { 1 : 100 , 2 : 200 }

print(len(x))
print(len(tuple))
print(len(dict))
# a method can be in different classes so the one that calls it will choose the one that is applied 


class Car : 
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self) :
        print("Drive")

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self) :
        print("Sail")

class Plane :
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self) :
        print("Fly")
car1 = Car("Ford" , "Mustang")
boat1 = Boat("Ibiza" , "Touring 20") 
plane1 = Plane("Boeing" , "747" )
for x in (car1 , boat1 , plane1) :
    x.move()


        
    