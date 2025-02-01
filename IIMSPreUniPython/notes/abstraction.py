from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod # this only affects the function right below 
    def drive(self) :
        print("Car is driving.")
        # this is not affected
    def new_fn(self) :
        print("My new fn.")

class Car(Vehicle) :
    pass 

car = Car() 
print(car.drive())

"""
Output:
error since the funtions is abstracted."""
