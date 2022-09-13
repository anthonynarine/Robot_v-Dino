from weapon import Weapon



from weapon import Weapon
from dinosaur import Dinosaur
import random

class Robot:
    def __init__(self, str_name):
        self.name = str_name
        self.health = random.randrange(70,100)
        self.active_weapon = Weapon("Longclaw", 15)

    def attack (self, dinosaur):
        pass

r1 = Robot("B9")
print(r1.name)
print(r1.health)
