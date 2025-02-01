import random
choices = ("rock" , "paper" , "scissors")
# tuple over list since we won't be changing them.
while True:
    user_ch = input("Enter rock , paper , scissors or e to stop (r,p,s,e):").lower()
    if user_ch in( "r" , "p" , "s" , "e")  :
        if user_ch == "e" :
            print("Thank you for playing.")
            quit()
        elif user_ch == "r" :
            user_ch = choices[0]
        elif user_ch =="p" :
            user_ch = choices[1]
        elif user_ch == "s" :
            user_ch = choices[2]
    else :
        print("Invalid Input.")
        continue
    computer = random.choice(choices)
    print(f"You:{user_ch}")
    print(f"Computer:{computer}")

    if (computer == choices[0] and user_ch == choices[1] )  or (computer == choices[1] and user_ch == choices[2]) or (computer == choices[2] and user_ch == choices[0]):
        print("You won!")
    elif (computer == choices[0] and user_ch == choices[2] )  or (computer == choices[2] and user_ch == choices[1]) or (computer == choices[1] and user_ch == choices[0]) :
        print("You lost.") 
# or put else you lose
    elif computer == user_ch :
        print("Draw!")






