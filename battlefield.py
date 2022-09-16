
from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur1 = None
        self.robot1 = None

    def welcome(self):
        print (f"\nWelcome to the epic battlefield where we'll see a Dinosaur battle a Robot, Let the fight begin!\n")

    def create_player(self):
        user1 = input("Enter the name of your Dinosaur: ")
        self.dinosaur1 = Dinosaur(user1)
        user2 = input("Enter the name of your Robot: ")
        self.robot1 = Robot(user2)
        print (f"Dino {self.dinosaur1.name} health = {self.dinosaur1.health}, Robot {self.robot1.name} Polwer level = {self.robot1.health}\n")              

    def battle_phase(self):
        self.dinosaur1.attack(self.robot1)
        self.robot1.attack(self.dinosaur1)
        
    def display_winner(self):
        if self.robot1.health <= 0:
            print (f"Robot {self.robot1.name} has been defeated") 
        else:
            if self.dinosaur1.health <= 0:
                print (f"Dinosaur {self.dinosaur1.name} has been defeated")        

    def run_game(self):
        self.welcome()
        self.create_player()
        while self.dinosaur1.health >=0 or self.robot1.health >=0:
            self.battle_phase()
        self.display_winner()

    
b1 = Battlefield
b1.run_game(b1)