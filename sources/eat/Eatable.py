import pygame.image
from pygame import Surface

from sources.common.Object import Object
from sources.screen_size import floor_height, screen_height


class Eatable(Object):
    image: Surface
    score: int
    y_pos: float

    def __init__(self, image_path: str):
        self.image = pygame.image.load(image_path)
        self.y_pos = screen_height - floor_height + 30
