
import random
from weapon import Weapon

class Robot:
    def __init__(self, str_name):
        self.name = str_name
        self.health = random.randint(90,100)
        self.active_weapon = Weapon("Longclaw")

    def attack (self, dinosaur):
        pass





