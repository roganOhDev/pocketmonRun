from typing import Tuple

import pygame
from pygame import Surface

from Game import Game

from dataclasses import dataclass


@dataclass
class Character:
    image: Surface
    size: Tuple[int, int]
    width: int
    height: int
    x_pos: float
    y_pos: float

    def __init__(self, image_root_path, image_path, stage_height):
        self.image = pygame.image.load(image_root_path + image_path)
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = (Game.screen_width / 2) - (self.width / 2)
        self.y_pos = Game.screen_height - self.height - stage_height

    def x_move(self, x_pos: int):
        self.x_pos = x_pos

        if self.x_pos < 0:
            self.x_pos = 0
        elif self.x_pos > Game.screen_width - self.width:
            self.x_pos = Game.screen_width - self.width

    def y_move(self, y_pos: int):
        self.y_pos = y_pos

    def get_rect(self):
        return self.image.get_rect()


