from dataclasses import dataclass

import pygame.image
from pygame.mixer import Sound
from pygame.surface import Surface


@dataclass
class Background:
    image: Surface
    bgm: Sound

    def __init__(self, image_path: str, bgm_path: str):
        self.image = pygame.image.load(image_path)
        self.bgm = pygame.mixer.Sound(bgm_path)
