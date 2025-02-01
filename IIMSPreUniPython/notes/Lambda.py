"""A lambda function is an anonymous function (i.e., defined without a name) that can take 
any number of arguments but, unlike normal functions, evaluates and returns only one 
expression. Note that, unlike a normal function, we don't surround the parameters of a 
lambda function with parentheses"""

x = lambda a : a + 10         # It is lamb da
print(x(5))
#Adds 10 to parameter of x (5+10) = 10
number = [1,2,3,4,5]
sqnumbers = list(map(lambda number: number ** 2))

