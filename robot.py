
import random
from weapon import Weapon

class Robot:
    def __init__(self, str_name):
        self.name = str_name.title()
        self.health = 100
        self.active_weapon = Weapon("Longclaw")

    def attack (self, dinosaur):
            dinosaur.health -= self.active_weapon.attack_power
            print(f"Robot: {self.name} has damaged {dinosaur.name} for {self.active_weapon.attack_power} health points {dinosaur.name} has {dinosaur.health} health points remaining\n")

       





