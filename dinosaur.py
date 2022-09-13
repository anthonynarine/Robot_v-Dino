import random
from robot import Robot


class Dinosaur:
    def __init__(self, str_name):
        self.name = str_name.title()
        self.health = random.randint(90,100)
        self.attack_power = random.randrange(15,25)

    def attack (self, robot):
        while robot.health > 0:
            print(f"\nRobot: {robot.name} current health = {robot.health}")
            robot.health -= self.attack_power
            print(f"Dino: {self.name} has damaged {robot.name} for {self.attack_power} health points {robot.name} has {robot.health} health points remaining\n")
            return
        else: 
           print (f"\nThe robot {robot.name}, has been defeated by the mighty dino {self.name}, the battle is over.\n")

            
        





