import random
class Fighter : 
    def __init__(self , name , health ):
        self.name = name 
        self.health = health 
        

class Warrior(Fighter) : 
    def details(self):
        return "Fighter class : Warrior , Health :100"
    
    def attack(self) :
        return random.randint(15 , 25)

class Mage(Fighter) :
    def details(self):
        return "Fighter class : Mage , Health :100"
    def attack(self) :
        return random.randint(10 , 30)

class Archer(Fighter) :
    def details(self):
        return "Fighter class : Archer , Health :100"
    def attack(self) :
        return random.randint(10 , 20)

def battle ():
    while True :
        name = input("Enter name:" )
        ch = input("choose your fihgter (warrior w , mage m , archer a )").lower()
        if ch == "w" :
            player = Warrior(name , 100)
        elif ch == "m" :
            player = Mage(name , 100)
        elif ch == "a" :
            player = Archer(name , 100)
        else :
            print("Invalid input.")
            continue
        flist = [Warrior("Computer" , 100),Mage("Computer" , 100),Archer("Computer" , 100)]
        computer = random.choice(flist)
        print(f"A {computer.details()} has appeared and has challenged you to a battle.")
        def fight() :
            while player.health >=0 and computer.health >= 0:
                computer.attack()
                player.attack()
                a = input("Enter to attack.")
                computer.health -= player.attack()
                player.health -= computer.attack()
                print(f"Player health ={player.health} , Computer health ={computer.health}")
            if player.health <=0:
                print("You lost.")
            elif computer.health <= 0:
                print("You Won.")
        while True:
            ch1 = input("Do you accept?(y/n) : ").lower()
            if ch1 == "y" :
                fight()
                quit()
            elif ch1 == 'n' :
                print("You lost because of being a coward.")
            else :
                print("Invalid Input.")
battle()


        
    