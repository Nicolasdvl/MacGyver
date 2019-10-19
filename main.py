from setup import *
from hero import *


setup = setup()
level = setup.loading_stage("level.txt")
hero = hero()
while hero.pos != "e":
    hero.movement(hero.pos, level)