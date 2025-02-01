
while True :
    num1 = float (input("Enter the first num: "))
    num2 = float (input("Enter the second num: "))
    ch = input("Enter an operator(+,-,*,/)")
    if ch == "+" :
        sum = num1 + num2 
        print(sum)
    elif ch == "-" :
        difference = num1 - num2 
        print(difference)
    elif ch == "*" :
        product = num1 * num2 
        print(product)
    elif ch == "/" :
        quotient = num2 / num1 
        print(quotient)
    else:
        print("Enter a valid operator.")
    ch1 = input("Do you want to continue? (y/n): ")
    if ch1 == "n" :
        break 