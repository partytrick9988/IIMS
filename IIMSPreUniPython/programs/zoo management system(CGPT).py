"""
welcome to virtual zoo 
1 add animal 
2 show animal 
3 calculate total food
4 exit
"""
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    
    def feed(self):
        print(f"{self.name} is now not hungry.")
        

    def make_sound(self):
        print(f"{self.name} the {self.species} says: {self.sound}")

    def info(self):
        print(f"Name: {self.name}, Species: {self.species}, Hunger Level: {self.hunger}/10")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self):
        name = input("Enter the animal's name: ")
        species = input("Enter the species: ")
        sound = input("What sound does it make? ")
        new_animal = Animal(name, species, sound)
        self.animals.append(new_animal)
        print(f"{name} the {species} has been added to the zoo!")

    def view_animals(self):
        if not self.animals:
            print("The zoo has no animals yet.")
            return
        print("\nAnimals in the Zoo:")
        for i, animal in enumerate(self.animals, 1):
            print(f"{i}. {animal.name} ({animal.species}) - Hunger: {animal.hunger}/10")

    def feed_animal(self):
        self.view_animals()
        if not self.animals:
            return
        choice = input("Choose an animal to feed by number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.animals):
            self.animals[int(choice) - 1].feed()
        else:
            print("Invalid choice.")

    def make_animal_sound(self):
        self.view_animals()
        if not self.animals:
            return
        choice = input("Choose an animal to hear its sound by number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.animals):
            self.animals[int(choice) - 1].make_sound()
        else:
            print("Invalid choice.")

    def run(self):
        while True:
            print("\nWelcome to the Virtual Zoo!")
            print("1. View Animals")
            print("2. Add an Animal")
            print("3. Feed an Animal")
            print("4. Hear an Animal Sound")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.view_animals()
            elif choice == "2":
                self.add_animal()
            elif choice == "3":
                self.feed_animal()
            elif choice == "4":
                self.make_animal_sound()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the Virtual Zoo
if __name__ == "__main__":
    zoo = Zoo()
    zoo.run()



    
