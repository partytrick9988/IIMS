"""A lambda function is an anonymous function (i.e., defined without a name) that can take 
any number of arguments but, unlike normal functions, evaluates and returns only one 
expression. Note that, unlike a normal function, we don't surround the parameters of a 
lambda function with parentheses"""

x = lambda a : a + 10         # It is lamb da
print(x(5))
#Adds 10 to parameter of x (5+10) = 10
number = [1,2,3,4,5]
sqnumbers = list(map(lambda x : x ** 2 , number))
"""The map() function takes two arguments:
A function to apply to each item (in this case, lambda x: x ** 2).
An iterable to process (in this case, the numbers list).
map() applies the lambda function to each element of the numbers list."""

"""Map in Python is a function that works as an iterator to return a result after applying a
 function to every item of an iterable (tuple, lists, etc.). It is used when you want to 
 apply a single transformation function to all the iterable elements. The iterable and 
 function are passed as arguments to the map in Python"""