import pygame
from hero import Hero

class Display():

    def __init__(self, config):
        """ Charge les images des objets et ouvre une fenêtre
        """

        self.hero = pygame.transform.scale(pygame.image.load(
            'ressource/MacGyver.png'), (config.sprite_height, config.sprite_width))
        self.guardian = pygame.transform.scale(pygame.image.load(
            'ressource/Gardien.png'), (config.sprite_height, config.sprite_width))
        self.needle = pygame.transform.scale(pygame.image.load(
            'ressource/aiguille.png'), (config.sprite_height, config.sprite_width))
        self.ether = pygame.transform.scale(pygame.image.load(
            'ressource/ether.png'), (config.sprite_height, config.sprite_width))
        self.tube = pygame.transform.scale(pygame.image.load(
            'ressource/tube_plastique.png'), (config.sprite_height, config.sprite_width))
        self.syringe = pygame.transform.scale(pygame.image.load(
            'ressource/seringue.png'), (config.inventory_sprite, config.inventory_sprite))
        self.wall = pygame.transform.scale(pygame.image.load(
            'ressource/wall.png'), (config.sprite_height, config.sprite_width))
        self.path = pygame.transform.scale(pygame.image.load(
            'ressource/path.png'), (config.sprite_height, config.sprite_width))
        self.window = pygame.display.set_mode(config.window)

    def __convert_pos_to_pixel(self, pos, config):
        """Converti l'indice de position d'un objet en coordonnées (x, y) exprimé en pixel
        """

        x_pixel_pos = int(pos * config.sprite_width -
                            ((pos - (pos % 15)) / 15 * config.window_width))
        y_pixel_pos = int((pos - (pos % 15)) /
                            15 * config.sprite_width)
        pixel_pos = (x_pixel_pos, y_pixel_pos)
        return pixel_pos

    def draw_window(self, config):
        """ Affiche une fenêtre et des instructions
        """
        self.window.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 25, True)
        text = font.render('Sortez du labyrinthe !', 1, (250,250,250))
        pixel_pos = self.__convert_pos_to_pixel(config.instruction_one, config)
        self.window.blit(text, pixel_pos)
        text = font.render('Usez des objets trouvés sur votre chemin', 1, (250,250,250))
        pixel_pos = self.__convert_pos_to_pixel(config.instruction_two, config)
        self.window.blit(text, pixel_pos)
        text = font.render('pour passer outre le guardien de la sortie.', 1, (250,250,250))
        pixel_pos = self.__convert_pos_to_pixel(config.instruction_three, config)
        self.window.blit(text, pixel_pos)
        pygame.display.update()
        pygame.time.wait(3000)
        

    def draw_items(self, item, image, config):
        """ Permet l'affichage d'objet
        item.pos : indice de la case sur lequel se trouve l'objet
        x_pixel_pos et y_pixel_pos : position de l'objet en pixel
        """

        if item.visibility == 1:
            pixel_pos = self.__convert_pos_to_pixel(item.pos, config)
            self.window.blit(image, pixel_pos)
        else:
            pass
        
    def draw_inventory(self, hero, config): 
        """Permet l'affichage de l'inventaire
        """
        font = pygame.font.SysFont('arial', 13, True)
        text = font.render('INVENTAIRE :', 1, (0,0,0))
        pixel_pos = self.__convert_pos_to_pixel(config.inventory_font, config)
        self.window.blit(text, pixel_pos)
        if 'syringe' in hero.inventory:
            pixel_pos = self.__convert_pos_to_pixel(config.inventory_one, config)
            self.window.blit(self.syringe, pixel_pos)
            pass
        else:
            if 'ether' in hero.inventory:
                self.ether = pygame.transform.scale(self.ether, (config.inventory_sprite, config.inventory_sprite))
                pixel_pos = self.__convert_pos_to_pixel(config.inventory_one, config)
                self.window.blit(self.ether, pixel_pos)
            if 'tube' in hero.inventory:
                self.tube = pygame.transform.scale(self.tube, (config.inventory_sprite, config.inventory_sprite))
                pixel_pos = self.__convert_pos_to_pixel(config.inventory_two, config)
                self.window.blit(self.tube, pixel_pos)
            if 'needle' in hero.inventory:
                self.needle = pygame.transform.scale(self.needle, (config.inventory_sprite, config.inventory_sprite))
                pixel_pos = self.__convert_pos_to_pixel(config.inventory_three, config)
                self.window.blit(self.needle, pixel_pos)


    def draw_labyrinth(self, level, config):
        """Parcours la liste level pour afficher un mur ou un passage
        pos : indice de la case parcouru
        x_pixel_pos et y_pixel_pos : position de l'objet en pixel
        """

        for pos, element in level.items():
            pixel_pos = self.__convert_pos_to_pixel(pos, config)
            if element == 'x':
                self.window.blit(self.wall, pixel_pos)
            else:
                self.window.blit(self.path, pixel_pos)
    
    def draw_final(self, config):
        if config.win:
            font = pygame.font.SysFont('arial', 35, True)
            text = font.render('Vous vous êtes échappez !', 1, (250,250,250))
            pixel_pos = self.__convert_pos_to_pixel(config.final, config)
            self.window.blit(text, pixel_pos)
            pygame.display.update()
            pygame.time.wait(3000)
        else:
            font = pygame.font.SysFont('arial', 35, True)
            text = font.render('Le guardien vous a attrapé !', 1, (250,250,250))
            pixel_pos = self.__convert_pos_to_pixel(config.final, config)
            self.window.blit(text, pixel_pos)
            pygame.display.update()
            pygame.time.wait(3000)
        


class Event():

    def __init__(self):
        pass

    def actions(self, level, hero):
        pygame.event.get()
        pygame.time.delay(100)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            hero.move(level, "up")
        elif keys[pygame.K_DOWN]:
            hero.move(level, "down")
        elif keys[pygame.K_LEFT]:
            hero.move(level, "left")
        elif keys[pygame.K_RIGHT]:
            hero.move(level, "right")
