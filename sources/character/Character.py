from dataclasses import dataclass
from enum import Enum

import pygame
from Game import Game
from pygame import Surface

from sources.character.skill.Health import Health
from sources.character.skill.Skill import Skill


class CharacterType(Enum):
    CHARMANDER = 1
    SQUIRTLE = 2
    BULBASAUR = 3


@dataclass
class Character:
    type: CharacterType
    image1: Surface
    image2: Surface
    width: float
    height: float
    skill: Skill
    life: float
    x_pos: float
    y_pos: float

    def __init__(self, image_path: str, skill: Skill):
        image = pygame.image.load(image_path)
        self.width = image.get_width()
        self.height = image.get_height()
        self.x_pos = 3
        self.y_pos = 3
        self.life = 100

        if isinstance(skill, Health):
            self.life *= Health().health_multiply

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
