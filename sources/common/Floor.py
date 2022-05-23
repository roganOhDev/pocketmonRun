import pygame
from pygame import Surface

from sources.game_set import screen_width, speed
from sources.images import BackgroundImage


class Floor:
    x_pos: float
    image = pygame.image.load(BackgroundImage.floor)
    scaled_image: Surface = pygame.transform.scale(image, (screen_width, image.get_height()))

    def __init__(self, x_pos):
        self.x_pos = x_pos

    def move(self):
        self.x_pos -= speed
