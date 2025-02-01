#Example 1 : Iterator
class My_iterator:
    def __init__(self , data):
        self.data = data 
        self.index = 0
    
    def __iter__ (self) :
        return self
    def __next__(self) :
        if self.index >= len(self.data):
            raise StopIteration
        print(f"Getting index : {self.index}")
        value = self.data[self.index]
        self.index += 1 
        return value 


# Example 2 : using iterator
my_list= [1,2,3,4,5] 
my_iter = My_iterator(my_list) 
for num in my_iter:
    print(num) 

#this is just to show how something is iterated no need to make the class 