import random


class Dinosaur:
    def __init__(self, str_name):
        self.name = str_name
        self.health = random.randrange(85,100)
        self.attack_power = int_attack_power = random.randrange(15,25)

    def attack (self, robot):
        pass

d1 = Dinosaur("Rexy")
print(d1.attack_power)
print(d1.health)