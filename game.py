import pygame
pygame.init()

class Display():
    """commentaire"""

    def __init__(self):
        self.hero = pygame.image.load('ressource/MacGyver.png')
        self.guardian = pygame.image.load('ressource/Gardien.png')
        self.needle = pygame.image.load('ressource/aiguille.png')
        self.ether = pygame.image.load('ressource/ether.png')
        self.tube = pygame.image.load('ressource/tube_plastique.png')
        self.wall = pygame.image.load('ressource/wall.png')
        self.path = pygame.image.load('ressource/path.png')
        self.window = pygame.display.set_mode((750,750))

    def draw_window (self):
        self.window.fill((0, 0, 0))
        pygame.display.update()
    
    def draw_items (self, item, image, setup):
        x_pixel_pos = int(item.pos * setup.sprite_width - ((item.pos -(item.pos % 15)) / 15 * setup.window_width))
        y_pixel_pos = int((item.pos - (item.pos % 15)) / 15 * setup.sprite_width)
        self.window.blit(image, (x_pixel_pos, y_pixel_pos))
        pygame.display.update()

    def draw_labyrinth (self, level, setup):
        for pos,element in enumerate(level):
            x_pixel_pos = int(pos * setup.sprite_width - ((pos -(pos % 15)) / 15 * setup.window_width))
            y_pixel_pos = int((pos - (pos % 15)) / 15 * setup.sprite_width)
            if element == 'p':
                self.window.blit(self.path, (x_pixel_pos, y_pixel_pos))
            elif element == 'x':
                self.window.blit(self.wall, (x_pixel_pos, y_pixel_pos))
        
        pygame.display.update()


    def transform_items (self, item, setup):
        item = pygame.transform.scale(item,(setup.sprite_height, setup.sprite_width))
        pygame.display.update()





