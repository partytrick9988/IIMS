import random

atp = 0
rnum = random.randint(0,10)
while True:
    atp += 1 
    ch = int(input("Enter a num: "))
    if ch == rnum:
        print("You guessed right.")
        quit()
    elif ch < rnum :
        print("Higher")
    elif ch > rnum :
        print("Lower")
    else : 
        print("Invalid input")
print(f"You guessed in {atp} times. ")
