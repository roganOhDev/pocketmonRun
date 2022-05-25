import pygame.image
from pygame import Surface

from sources.common.Object import Object
from sources.game_set import floor_height, screen_height, screen_width


class Eatable(Object):
    image: Surface
    score: int
    y_pos: float

    def __init__(self, image_path: str, y_fix: float):

        image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.rotozoom(image, 0, 0.2)

        default_y_pos = screen_height - floor_height - self.image.get_height() - 50

        y_fix = default_y_pos if y_fix == 0 else y_fix

        super().__init__(self.image, screen_width, y_fix)
