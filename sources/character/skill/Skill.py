from dataclasses import dataclass

import pygame
from pygame.surface import Surface

from sources.common.Object import Object
from sources.character.skill.Type import SkillType


@dataclass
class Skill(Object):
    image1: Surface
    image2: Surface
    width: float
    height: float
    type: SkillType
    time: int
    delay: int
    current_image: Surface
    current_image_bool: bool

    def __init__(self, image: str):
        if image:
            image = pygame.image.load(image)
            self.current_image = image
            self.current_image_bool = True

    def update_motion(self):
        self.current_image = self.image1 if self.current_image_bool else self.image2
        self.current_image_bool = not self.current_image_bool