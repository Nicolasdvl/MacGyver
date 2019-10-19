from setup import *
from hero import *
from guardian import *


setup = setup()
level = setup.loading_stage("level.txt")
hero = hero(level)
guardian = guardian(level)
while setup.run == True:
    hero.movement(hero.pos, level)
    guardian.is_there_anyone_here(hero.pos, guardian.pos, setup.run)