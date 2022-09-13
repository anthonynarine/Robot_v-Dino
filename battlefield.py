from dinosaur import Dinosaur


from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("str_name")
        self.robot = Robot("str_name")
    
    def run_game(self):
        pass
    
    def display_welcome(self):
        print (f"Welcome to this epic battle of {self.dinosaur()} the dinosaur vs. {self.robot()}, the robot.")

    def battle_phase(self):
        
        pass

    def display_winner(self):
        pass