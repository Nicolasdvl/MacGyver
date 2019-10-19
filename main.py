import setup
import hero


setup = setup()
level = setup.loading_stage("level.txt")
hero = hero()
hero.movement(hero.pos)