"""
Arithmetic Operators
__add__(self, other)     # Addition
__sub__(self, other)     # Subtraction
__mul__(self, other)     # Multiplication
__floordiv__(self, other) # Floor Division
__truediv__(self, other) # True Division
__mod__(self, other)     # Modulo
__pow__(self, other)     # Power

# Bitwise Operators
__and__(self, other)     # Bitwise AND
__or__(self, other)      # Bitwise OR
__xor__(self, other)     # Bitwise XOR
__invert__(self)         # Bitwise NOT
__lshift__(self, other)  # Left Shift
__rshift__(self, other)  # Right Shift

# Comparison Operators
__lt__(self, other)      # Less Than
__le__(self, other)      # Less Than or Equal
__gt__(self, other)      # Greater Than
__ge__(self, other)      # Greater Than or Equal
__eq__(self, other)      # Equals
__ne__(self, other)      # Not Equal

# Unary Operators
__pos__(self)            # Unary Positive
__neg__(self)            # Unary Negative

# Container and Sequence Methods
__contains__(self, item) # Containment (in)
__len__(self)            # Length
__getitem__(self, key)   # Indexing
__setitem__(self, key, value) # Setting Item
__delitem__(self, key)   # Deleting Item
__iter__(self)           # Iteration
__next__(self)           # Next Item

# Callable and Conversion Methods
__call__(self, *args, **kwargs) # Call
__str__(self)            # String Conversion
__repr__(self)           # Representation
__hash__(self)           # Hashing
__bool__(self)           # Boolean Value
__abs__(self)            # Absolute Value
__round__(self, n)       # Round
__reversed__(self)       # Reversed
"""


class Vector :
    def __init__(self , x , y): 
        self.x = x 
        self.y = y

    """
    this make changes to the meaning of the + operator the __add__ ensures that 
    when + operator is used then this methods works only for other data types 
    it will still work the same for basic stuff
    """
    def __add__(self, *others) : 
        sum_vector = Vector(self.x , self.y) 
        for other in others :
            sum_vector = Vector(sum_vector.x + other.x , sum_vector.y + other.y)
        return sum_vector
    def __sub__(self, *others) : 
        sub_vector = Vector(self.x , self.y) 
        for other in others :
            sub_vector = Vector(sub_vector.x - other.x , sub_vector.y - other.y)
        return sub_vector
    def __mul__(self, *others) : 
        mul_vector = Vector(self.x , self.y) 
        for other in others :
            mul_vector = Vector(mul_vector.x * other.x , mul_vector.y * other.y)
        return mul_vector
    def __truediv__(self, *others) : 
        truediv_vector = Vector(self.x , self.y) 
        for other in others :
            truediv_vector = Vector(truediv_vector.x / other.x , truediv_vector.y / other.y)
        return truediv_vector
    def __floordiv__(self, *others) : 
        floordiv_vector = Vector(self.x , self.y) 
        for other in others :
            floordiv_vector = Vector(floordiv_vector.x // other.x , floordiv_vector.y // other.y)
        return floordiv_vector
    def __mod__(self, *others) : 
        mod_vector = Vector(self.x , self.y) 
        for other in others :
            mod_vector = Vector(mod_vector.x % other.x , mod_vector.y % other.y)
        return mod_vector
    def __pow__(self, *others) : 
        pow_vector = Vector(self.x , self.y) 
        for other in others :
            pow_vector = Vector(pow_vector.x ** other.x , pow_vector.y ** other.y)
        return pow_vector
    def __str__(self):
        return f"Vector: ({self.x} , {self.y})"
    

v1 = Vector(5,6)
v2 = Vector(7,8)
v3 = Vector(9,10) # we can add this to the operations as well just did not like (v1 + v2 + v3 and so on )
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 / v2)
print(v1 // v2)
print(v1 % v2)
print(v1 ** v2)