from dataclasses import dataclass

from pygame.surface import Surface


@dataclass
class Background:
    image: Surface
    bgm: str

