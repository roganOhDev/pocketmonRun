from typing import Tuple

import pygame.font
from pygame import Surface
from pygame.font import Font


class Text:
    font: Font
    text: str
    color: Tuple
    x_pos: float
    y_pos: float

    def __init__(self, font_size: int, x_pos: float, y_pos: float, text: str, color: Tuple):
        self.font = pygame.font.Font(None, font_size)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.color = color
