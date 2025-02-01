import random

class Fighter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0


class Warrior(Fighter):
    def get_details(self):
        return f"Fighter class: Warrior, Health: {self.health}"

    def attack(self):
        return random.randint(15, 25)


class Mage(Fighter):
    def get_details(self):
        return f"Fighter class: Mage, Health: {self.health}"

    def attack(self):
        return random.randint(10, 30)


class Archer(Fighter):
    def get_details(self):
        return f"Fighter class: Archer, Health: {self.health}"

    def attack(self):
        return random.randint(10, 20)


def choose_fighter(name):
    while True:
        choice = input("Choose your fighter (warrior [w], mage [m], archer [a]): ").lower()
        if choice == "w":
            return Warrior(name, 100)
        elif choice == "m":
            return Mage(name, 100)
        elif choice == "a":
            return Archer(name, 100)
        else:
            print("Invalid input. Please choose again.")


def perform_fight(player, computer):
    round_counter = 1
    print(f"A {computer.get_details()} has appeared and has challenged you to a battle!")
    while player.is_alive() and computer.is_alive():
        input(f"\n[Round {round_counter}] Press Enter to attack...")
        player_damage = player.attack()
        computer_damage = computer.attack()

        computer.health = max(0, computer.health - player_damage) # the first arg says what is the minimum value of the second arg
        player.health = max(0, player.health - computer_damage) # this is similar to writing [if health <= 0 :] min ensures max value and vice versa
#                                                                                            [   health = 0   ]

        print(f"{player.name} dealt {player_damage} damage. {computer.name}'s health: {computer.health}")
        print(f"{computer.name} dealt {computer_damage} damage. {player.name}'s health: {player.health}")
        round_counter += 1

    if player.is_alive():
        print("\nYou won the battle!")
    else:
        print("\nYou lost the battle.")


def main():
    print("Welcome to the battle arena!")
    name = input("Enter your name: ")
    player = choose_fighter(name)

    enemy_classes = [Warrior("Computer", 100), Mage("Computer", 100), Archer("Computer", 100)]
    computer = random.choice(enemy_classes)

    while True:
        accept = input("Do you accept the challenge? (y/n): ").lower()
        if accept == "y":
            perform_fight(player, computer)
            break
        elif accept == "n":
            print("You lost because of being a coward.")
            break
        else:
            print("Invalid input. Please type 'y' or 'n'.")


if __name__ == "__main__":
    main()
