import pygame.transform
from pygame import Surface

from sources.common.Object import Object
from sources.game_set import screen_width


class Trap(Object):
    def __init__(self, image: Surface, y_pos: float):
        super().__init__(image, screen_width, y_pos)

    def get_height(self) -> float:
        return self.image.get_height()
