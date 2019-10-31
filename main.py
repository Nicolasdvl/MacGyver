from setup import Setup
from hero import Hero
from guardian import Guardian
from items import Items

setup = Setup()
level = setup.loading_stage("level.txt")
hero = Hero(level)
guardian = Guardian(level)
needle = Items("needle", level)
ether = Items("ether", level)
tube = Items("tube", level)

while setup.run == True:
    hero.pos = hero.movement(hero.pos, level)
    hero.pick(hero.inventory, needle.pos, needle.name, hero.pos)
    hero.pick(hero.inventory, ether.pos, ether.name, hero.pos)
    hero.pick(hero.inventory, tube.pos, tube.name, hero.pos)
    hero.craft(hero.inventory)
    setup.run = guardian.is_there_anyone_here(hero.pos, guardian.pos, setup.run, hero.inventory)