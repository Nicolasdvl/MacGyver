from setup import Setup
from hero import Hero
from guardian import Guardian
from items import Items
from game import Display
import pygame


def main():
    pygame.init()
    setup = Setup()
    display = Display()
    level = setup.loading_stage("level.txt")
    hero = Hero(level)
    guardian = Guardian(level)
    needle = Items("needle", level)
    ether = Items("ether", level)
    tube = Items("tube", level)
    display.draw_window()

    while setup.run == True:
        
        hero.move(level)
        hero.pick(needle)
        hero.pick(ether)
        hero.pick(tube)
        hero.craft()
        #display.transform_items()
        display.draw_labyrinth(level, setup)
        display.draw_items(hero, display.hero, setup)

        setup.run = guardian.is_there_anyone_here(hero, setup)

main()