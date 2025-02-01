"""   parent class = derived class
single 
multiple: from 2 parents
multilevel : from grand parent
hierarchial : multiple child one parent
hybrid
"""
 
#super().__init_  -> Used to inherit form parent class

#Multiple inheritance
def multiple_inheritance():
    class Father :
        def __init__(self):
            print("Father class constructor.")
        def father_method(self):
            print("Father give money.") 
    class Mother :
        def __init__(self):
            print("Mother class constructor.")
        def mother_method(self):
            print("Mother give money.") 

    class Child(Father , Mother) :
        def __init__(self):
            super().__init__() # here super() represents the parent class (first one father) instead the name of the class can be written here.
            print("Child class constructor.")

    #Now both the constructor methods of father and mother can be called by the child.
    child1 = Child()
    child1.father_method()  # if there was such a method in the child class then it would not pull from the parent but from the child.
    child1.mother_method() 
multiple_inheritance()

#Multilevel inheritance

def multilevel_inheritance():
    class Grand_Father :
        def __init__(self):
            print("GrandFather class constructor.")
        def grandfather_method(self):
            print("GrandFather give money.") 
    class Father(Grand_Father) :
        def __init__(self):
            print("Father class constructor.")
        def father_method(self):
            print("Father give money.") 
    class Child(Father) :
        def __init__(self):           
            print("Child class constructor.")
    child1 = Child()
    child1.grandfather_method()
multilevel_inheritance() 

#heirarchial inheritance
def heirarchial_inheritance():
    class Father :
        def __init__(self):
            print("Father class constructor.")
        def father_method(self):
            print("Father give money.") 
    class Child1(Father) :
        def __init__(self):
            print("Child1 class constructor.") 
    class Child2(Father) :
        def __init__(self):           
            print("Child2 class constructor.")
    child1 = Child1()
    child2 = Child2()
    child1.father_method()
    child2.father_method()
heirarchial_inheritance ()
 

class Shape :
    def __init__(self , color):
        self.color = color
    def area(self) :
        print("Area method of shape class.")

class Circle(Shape) :
    def __init__(self, color , radius):
        super().__init__(color)
        self.radius = radius
    def area(self) :
        print("Area method of class circle.")


class Rectangle(Shape) :
    def __init__(self, color , lenght , breath):
        super().__init__(color)
        self.lenght = lenght
        self.breath = breath
    def area(self) :
        print("Area method of class rectangle.")

