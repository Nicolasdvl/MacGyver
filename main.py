from setup import *
from hero import *
from guardian import *
from items import *

setup = setup()
level = setup.loading_stage("level.txt")
hero = hero(level)
guardian = guardian(level)
needle = items("needle", level)
ether = items("ether", level)
tube = items("tube", level)

while setup.run == True:
    hero.pos = hero.movement(hero.pos, level)
    hero.pick(hero.inventory, needle.pos, needle.name, hero.pos)
    hero.pick(hero.inventory, ether.pos, ether.name, hero.pos)
    hero.pick(hero.inventory, tube.pos, tube.name, hero.pos)
    guardian.is_there_anyone_here(hero.pos, guardian.pos, setup.run)
    print(hero.inventory)