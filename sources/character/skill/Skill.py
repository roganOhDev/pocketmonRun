from dataclasses import dataclass

import pygame
from pygame.surface import Surface

from sources.character.skill.Type import SkillType


@dataclass
class Skill:
    image1: Surface
    image2: Surface
    width: float
    height: float
    type: SkillType
    time: int
    delay: int

    def __init__(self, image: str):
        if image:
            image = pygame.image.load(image)
            self.width = image.get_width()
            self.height = image.get_height()

