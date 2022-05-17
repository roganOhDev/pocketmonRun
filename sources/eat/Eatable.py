import pygame.image
from pygame import Surface

from sources.Object import Object


class Eatable(Object):
    image: Surface
    score: int
    x_pos: float
    y_pos: float

    def __init__(self, image_path: str):
        self.image = pygame.image.load(image_path)
