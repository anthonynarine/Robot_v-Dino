
import random
from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon




r1 = Robot("tin_man")
d1 = Dinosaur("Rexy")


r1 = Robot("tin_man")
d1 = Dinosaur("Rexy")


print(r1.name)
print(r1.active_weapon.name)
print(r1.health)

print ("\nV\n")

print(d1.name)
print(d1.health)
print(d1.attack_power)


d1.attack(r1)
print(r1.health)
d1.attack(r1)

