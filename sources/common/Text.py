from typing import Tuple

import pygame.font
from pygame import Surface
from pygame.font import Font

from sources.game_set import screen_width, screen_height


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

    def render(self) -> Surface:
        return self.font.render(self.text, True, self.color)

    def get_pos(self) -> Tuple:
        return self.x_pos, self.y_pos

    @staticmethod
    def get_pos_to_center(rendered_text: Surface):
        return rendered_text.get_rect(center=(screen_width / 2, screen_height / 2))
