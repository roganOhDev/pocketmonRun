from dataclasses import dataclass

from sources.Background import Background
from sources.character.Bulbasaur import Bulbasaur
from sources.character.Character import Character, CharacterType
from sources.character.Charmander import Charmander
from sources.character.Squirtle import Squirtle
from sources.eat.Eatable import Eatable
from sources.images import BackgroundImage
from sources.musics import BackgroundMusic


@dataclass
class Game:
    character: Character
    background: Background
    score: int

    screen_width: int = 960
    screen_height: int = 450
    fps: int = 50
    speed: float = 5 / fps

    def __init__(self, ):
        self.background = Background(BackgroundImage.default_background, BackgroundMusic.default)
        self.score = 0

    def bonus_stage(self, background: Background):
        self.background = background

    def choose_character(self):
        print("have to implement")

    def create_character(self, character_type: CharacterType):
        if character_type is CharacterType.SQUIRTLE:
            self.character = Squirtle()
        elif character_type is CharacterType.CHARMANDER:
            self.character = Charmander()
        elif character_type is CharacterType.BULBASAUR:
            self.character = Bulbasaur()

    def add_score(self, element: Eatable):
        self.score += element.score
