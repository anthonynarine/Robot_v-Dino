import random
from robot import Robot


class Dinosaur:
    def __init__(self, str_name):
        self.name = str_name.title()
        self.health = 100
        self.attack_power = random.randint(15,20)

    def attack (self, robot):
        robot.health -= self.attack_power
        print(f"Dino {self.name} has damaged {robot.name} for {self.attack_power} health points {robot.name} has {robot.health} health points remaining\n")



            
        




