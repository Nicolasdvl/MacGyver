import pygame

from config import Config
from hero import Hero
from guardian import Guardian
from items import Items
from game import Display, Event


def main():
    """Début du programme
    """

    pygame.init()
    pygame.font.init()
    config = Config()
    display = Display(config)
    level = config.loading_stage("level.txt")
    hero = Hero(level)
    guardian = Guardian(level)
    needle = Items("needle", level)
    ether = Items("ether", level)
    tube = Items("tube", level)
    keys = Event()
    display.draw_window(config)

    while config.run:

        display.draw_labyrinth(level, config)
        keys.actions(level, hero)
        hero.pick(needle)
        hero.pick(ether)
        hero.pick(tube)
        hero.craft()
        display.draw_items(hero, display.hero, config)
        display.draw_items(guardian, display.guardian, config)
        display.draw_items(ether, display.ether, config)
        display.draw_items(needle, display.needle, config)
        display.draw_items(tube, display.tube, config)
        display.draw_inventory(hero, config)
        guardian.is_there_anyone_here(hero, config)
        pygame.display.update()
    display.draw_final(config)


if __name__ == "__main__":
    main()
