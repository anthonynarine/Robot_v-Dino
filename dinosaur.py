import random
from robot import Robot


class Dinosaur:
    def __init__(self, str_name):
        self.name = str_name
        self.health = random.randint(90,100)
        self.attack_power = random.randrange(15,25)

    def attack (self, robot):
        while robot.health > 0:
            print(f"\n{robot.name} health is {robot.health}")
            robot.health -= self.attack_power
            print(f"{self.name} has damaged {robot.name} for {self.attack_power} health points {robot.name} has {robot.health} health points remaining")
        else: 
           print (f"\n{robot.name} has been defeated by the mighty {self.name} the battle is over")

            
        





