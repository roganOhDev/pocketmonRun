from dataclasses import dataclass

from sources.Background import Background
from sources.character.Character import Character, CharacterType
from sources.images import BackgroundImage
from sources.musics import BackgroundMusic


@dataclass
class Game:
    character: Character
    background: Background

    screen_width: int = 640
    screen_height: int = 480
    fps: int = 50
    speed: float = 5 / fps

    def __init__(self, ):
        self.background = Background(BackgroundImage.default_background, BackgroundMusic.default)

    def bonus_stage(self, background: Background):
        self.background = background

    def choose_character(self, character_type: CharacterType):
        self.character = character_type


