import pygame.image
from pygame import Surface

from sources.common.Object import Object
from sources.game_set import floor_height, screen_height, screen_width


class Eatable(Object):
    image: Surface
    score: int
    y_pos: float

    def __init__(self, image_path: str):

        image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.rotozoom(image, 0, 0.1)

        super().__init__(self.image, screen_width - self.image.get_width(),
                         screen_height - floor_height - self.image.get_height() - 5)
