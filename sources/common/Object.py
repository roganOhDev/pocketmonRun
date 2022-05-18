from pygame import Surface
from dataclasses import dataclass


@dataclass()
class Object:
    x_pos: float
    y_pos: float

    def position_update_character_run(self, x_pos):
        self.x_pos = x_pos

    @staticmethod
    def get_width(image: Surface) -> int:
        return image.get_width()

    @staticmethod
    def get_height(image: Surface) -> int:
        return image.get_height()
