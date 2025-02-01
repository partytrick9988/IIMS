import random

class Treasure :
    
    def __init__(self , name  , value):
        self.name = name 
        self.value = value 
        
    def __str__(self):
        return f"{self.name} worth {self.value} goldcoins." 

class Room : 
    
    def __init__(self , name , treasures = None) :
        self.name = name  
        self.treasures = treasures if treasures else [] 
    
    def add_treasure (self , treasure ) :
        self.treasures.append(treasure) 
    
    def __iter__(self):
        return iter(self.treasures) 
    
    def __str__(self):  # remove the self here 
        treasure_names = ' , '.join([str(treasure) for treasure in self.treasures])
        return f"Room : {self.name} | Treasures : {treasure_names}"

class Player :
    
    def __init__(self , name ):
        self.name = name 
        self.treasure_found = 0
    
    def find_treasure(self, treasure ) :
        self.treasure_found += treasure.value
        print(f"{self.name} found {treasure}")
    
    def __str__(self):
        return f"{self.name} has found {self.treasure_found} gold coins."

class Game:
    
    def __init__(self , rooms , player ): 
        self.rooms = rooms 
        self.player = player
        self.attempts = 3 
    
    def attempt_to_find_treasure(self , room) :
        while self.attempts > 0 :
            print(f"\n {self.player} - You have {self.attempts -1 } attempts to find a treasure in {room}")
            self.attempts -= 1 
            for treasure in room :
                self.player.find_treasure(treasure) 
                room.treasures.remove(treasure) 
                return True
            
            print(f"Sorry, You didn't find any treasure in {room.name}.")
            return False
            
    def play(self) : 
        print(f"{self.player} starts the game \n")

        while self.rooms and self.attempts > 0 :
            print(f"\n Rooms available to explore." ) 
            for idx , room in enumerate(self.rooms) :
                print(f"{idx+1}. {room.name}")
            
            room_choice = int(input("Enter the room number to explore : ")) 
            if 1 <= room_choice <= len(self.rooms) :
                selected_room = self.rooms.pop(room_choice -1 ) 
                self.treasure_found = self.attempt_to_find_treasure(selected_room)
            else :
                print("Invalid room number. Please try again.") 
        print(f"\n No more attempts left.")
        print(self.player) 

def setup_game() :
    treasure_list = [
        Treasure("Golden Crown " , 100 ),
        Treasure("Silver sword " , 40 ),
        Treasure("Ruby Necklace " , 200 ),
        Treasure("Ancient Coin " , 300 ),
        Treasure("Diamond Necklace " , 80 ),
    ]

    rooms = [
        Room("kitchen" , [random.choice (treasure_list)]),
        Room("Bedroom" , [random.choice (treasure_list)]),
        Room("Living Room" , [random.choice (treasure_list)]),
        Room("Dining" , [random.choice (treasure_list)]),
        Room("Bathroom" , [random.choice (treasure_list)]),
        Room("Office" , [random.choice (treasure_list)]),
        Room("Garden" , [random.choice (treasure_list)]),
        Room("Basement" , [random.choice (treasure_list)]),
        Room("Library" , [random.choice (treasure_list)]),
        Room("Workshop" , [random.choice (treasure_list)]),
    ]
    player_name = input("Enter your name :")
    player = Player(player_name)

    game = Game (rooms , player )
    game.play()

setup_game()