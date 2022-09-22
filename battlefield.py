
from dinosaur import Dinosaur
from robot import Robot
import random
import time

class Battlefield:
    def __init__(self):
        self.dinosaur = ""  
        self.robot = ""

    def create_player(self):
        user1 = input("Enter the name of your Dinosaur: ")
        self.dinosaur = Dinosaur(user1)

        user2 = input("Enter the name of your Robot: ")
        self.robot = Robot(user2)
        print (f"Dino {self.dinosaur.name} health = {self.dinosaur.health} ~ Robot {self.robot.name} Power level = {self.robot.health}\n")              

    def welcome(self):
        print (f"\nWelcome to the epic battlefield where we'll see a Dinosaur battle a Robot, Let the fight begin!\n")



    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            attack_turn = random.randint(1,2)
            time.sleep(1)
            if attack_turn == 1:
                print ("Dino attacked")
                self.dinosaur.attack(self.robot)
            elif attack_turn == 2:
                time.sleep(1)
                print ("Robo attacked")
                self.robot.attack(self.dinosaur)


    def display_winner(self):
        if self.robot.health <= 0:
            print (f"Robot {self.robot.name} has been pummeled into a pile a scrap metal") 
        elif self.dinosaur.health <=  0:
            print (f"Dinosaur {self.dinosaur.name} was vaporized to extinction")        


    def run_game(self):
        self.welcome()
        time.sleep(1)
        self.create_player()
        time.sleep(1)
        self.battle_phase()
        time.sleep(1)
        self.display_winner()
 


b = Battlefield()
b.run_game()