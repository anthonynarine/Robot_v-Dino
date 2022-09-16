import random

class Weapon: 
    def __init__(self, str_name):
        self.name = str_name
        self.attack_power = random.randint(15,20)


