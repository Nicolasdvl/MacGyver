import pygame
pygame.init()

class Display():

    def __init__(self):

        """ Charge les images des objets et ouvre une fenêtre
        """

        self.hero = pygame.image.load('ressource/MacGyver.png')
        self.guardian = pygame.image.load('ressource/Gardien.png')
        self.needle = pygame.image.load('ressource/aiguille.png')
        self.ether = pygame.image.load('ressource/ether.png')
        self.tube = pygame.image.load('ressource/tube_plastique.png')
        self.wall = pygame.image.load('ressource/wall.png')
        self.path = pygame.image.load('ressource/path.png')
        self.window = pygame.display.set_mode((750,750))

    def draw_window (self):

        """ Affiche une fenêtre
        """

        self.window.fill((0, 0, 0))
        pygame.display.update()
    
    def draw_items (self, item, image, setup):

        """ Permet l'affichage d'objet
        item.pos : indice de la case sur lequel se trouve l'objet
        x_pixel_pos et y_pixel_pos : position de l'objet en pixel
        """
        
        x_pixel_pos = int(item.pos * setup.sprite_width - ((item.pos -(item.pos % 15)) / 15 * setup.window_width))
        y_pixel_pos = int((item.pos - (item.pos % 15)) / 15 * setup.sprite_width)
        self.window.blit(image, (x_pixel_pos, y_pixel_pos))
        pygame.display.update()

    def draw_labyrinth (self, level, setup):

        """ Parcours la liste level pour afficher un mur ou un passage
        pos : indice de la case parcouru
        x_pixel_pos et y_pixel_pos : position de l'objet en pixel
        """

        for pos,element in enumerate(level):
            x_pixel_pos = int(pos * setup.sprite_width - ((pos -(pos % 15)) / 15 * setup.window_width))
            y_pixel_pos = int((pos - (pos % 15)) / 15 * setup.sprite_width)
            if element == 'p':
                self.window.blit(self.path, (x_pixel_pos, y_pixel_pos))
            elif element == 'x':
                self.window.blit(self.wall, (x_pixel_pos, y_pixel_pos))
        
        pygame.display.update()


    def transform_items (self, item, setup):

        """ Permets de redimensionner l'image aux dimensions d'un sprite
        """

        item = pygame.transform.scale(item,(setup.sprite_height, setup.sprite_width))
        pygame.display.update()

class Input():

    def __init__(self):
        self = None

    def get_keys(self):
        pygame.event.get()
        pygame.time.delay(100)
        self = pygame.key.get_pressed()




