class Person: 
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def greet(self) :
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    def __str__(self):
        return f"Person(name={self.name} , age = {self.age})"
    

ruman = Person("ruman", 28 ) # possible befcause of __init__ and greet()
ruman.greet()   
Person("ruman" , 28 ).greet()
print(ruman.name)
print(ruman.age)


print(ruman)   # possible because of __str__(self)


class Pet() :  # same as [class Pet:]
    def __init__(self , name , age):
        self.name = name 
        self.age = age
    def show(self) : 
        print(f"I am {self.name} and I am {self.age} years old.")

class Dog(Pet) :
    def __init__(self, name, age , color , breed):
        super().__init__(name, age)
        self.color = color
        self.breed = breed
    def speak(self) :
        print("Bark")

class Cat(Pet) :
    def __init__(self, name, age , color ):
        super().__init__(name, age)
        self.color = color
    def speak(self) :
        print("Meow")


dog1 = Dog("Tom", 5 , "brown" , "lab" )
dog1.show()
dog1.speak()

cat1 = Cat("jerry", 2 , "white")
cat1.show()
cat1.speak()