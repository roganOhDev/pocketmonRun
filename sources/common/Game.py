from dataclasses import dataclass

import pygame.display

from sources.common.Background import Background
from sources.common.Time import Time
from sources.character.Bulbasaur import Bulbasaur
from sources.character.Character import Character, CharacterType
from sources.character.Charmander import Charmander
from sources.character.Squirtle import Squirtle
from sources.eat.Eatable import Eatable
from sources.images import BackgroundImage, BulbasaurImage, SquirtleImage, CharmanderImage
from sources.musics import BackgroundMusic


@dataclass
class Game:
    character: Character
    background: Background
    score: int
    time: Time
    speed: float
    screen_width: int = 960
    screen_height: int = 450

    def __init__(self):
        self.background = Background(BackgroundImage.default_background, BackgroundMusic.default, self.screen_width,
                                     self.screen_height)
        self.time = Time()
        self.speed = 5 / self.time.fps
        self.score = 0
        self.character = self.choose_character()

    def start_game(self):
        self.background.show_default_screen(self.screen_width, self.screen_height)

    def bonus_stage(self, background: Background):
        self.background = background

    def choose_character(self) -> Character:
        self.background.screen.fill(pygame.Color("white"))
        self.background.choose_character_screen(self.background.screen)
        screen = self.background.screen
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        while True:
            for event in (pygame.event.get()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 < event.pos[0] < screen_width / 2 and 0 < event.pos[1] < screen_height / 2:
                        return self.create_character(CharacterType.CHARMANDER)

                    elif 0 < event.pos[0] < screen_width / 2 and screen_height / 2 < event.pos[1] < screen_height:
                        return self.create_character(CharacterType.BULBASAUR)

                    elif screen_width / 2 < event.pos[0] < screen_width and \
                            screen_height / 2 < event.pos[1] < screen_height:
                        return self.create_character(CharacterType.SQUIRTLE)

    @staticmethod
    def create_character(character_type: CharacterType):
        if character_type is CharacterType.SQUIRTLE:
            return Squirtle(SquirtleImage.image1)
        elif character_type is CharacterType.CHARMANDER:
            return Charmander(CharmanderImage.image_1)
        elif character_type is CharacterType.BULBASAUR:
            return Bulbasaur(BulbasaurImage.image_1)

    def add_score(self, element: Eatable):
        self.score += element.score
