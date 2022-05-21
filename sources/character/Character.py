from dataclasses import dataclass
from enum import Enum

import pygame
from pygame import Surface

from sources.character.CharacterStatus import CharacterStatus
from sources.character.skill.Health import Health
from sources.character.skill.Skill import Skill
from sources.images import CharmanderImage, SquirtleImage, BulbasaurImage, BackgroundImage
from sources.scrren_size import *

character_x_pos = 3


class CharacterType(Enum):
    CHARMANDER = 1
    SQUIRTLE = 2
    BULBASAUR = 3


@dataclass
class Character:
    type: CharacterType
    status: CharacterStatus
    current_image: Surface
    current_image_bool: bool
    image1: Surface
    image2: Surface
    skill: Skill
    life: float
    x_pos: float
    y_pos: float
    to_x: float
    to_y: float
    y_speed: float

    floor_height = pygame.image.load(BackgroundImage.floor).get_height()

    def __init__(self, image1_path: str, skill: Skill):
        image = pygame.image.load(image1_path)
        self.to_x = 0
        self.to_y = 0
        self.x_pos = character_x_pos
        self.current_image = image
        self.current_image_bool = True
        self.status = CharacterStatus.RUNNING
        self.y_pos = screen_height - self.floor_height - self.current_image.get_height()
        self.y_speed = 0
        self.life = 100

        if isinstance(skill, Health):
            self.life *= Health().health_multiply

    def update_motion(self):
        self.current_image = self.image1 if self.current_image_bool else self.image2
        self.current_image_bool = not self.current_image_bool


    def y_move(self, y_pos: float):
        self.y_pos = y_pos

    def jump(self):
        self.y_speed = 5
        self.status = CharacterStatus.JUMPING

    def jumping(self):
        if -5 <= self.y_speed <= 5:
            self.y_move(self.y_pos + self.y_speed)
            self.y_speed -= 1

        elif self.y_speed < -5 or self.y_pos <= self.floor_height:
            self.jump_stop()

    def jump_stop(self):
        self.y_pos = self.floor_height
        self.y_speed = 0
        self.status = CharacterStatus.RUNNING

    def slide(self):
        self.y_pos = self.floor_height
        self.y_speed = 0
        self.status = CharacterStatus.SLIDING
        self.current_image = self.get_slide_image()

    @staticmethod
    def get_slide_image() -> Surface:
        image_path = ""
        if type is CharacterType.CHARMANDER:
            image_path = CharmanderImage.slide_1
        elif type is CharacterType.SQUIRTLE:
            image_path = SquirtleImage.slide
        elif type is CharacterType.BULBASAUR:
            image_path = BulbasaurImage.slide

        return pygame.image.load(image_path)
