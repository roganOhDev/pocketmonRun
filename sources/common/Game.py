from dataclasses import dataclass
import random

import pygame.display

from sources.character.Bulbasaur import Bulbasaur
from sources.character.Character import Character, CharacterType
from sources.character.Character import character_x_pos
from sources.character.Charmander import Charmander
from sources.character.Squirtle import Squirtle
from sources.common.Background import Background
from sources.common.Object import Object
from sources.common.Time import Time
from sources.eat.Bonus.Bonus import Bonus
from sources.eat.Bonus.BonusCoin import BonusCoin
from sources.eat.Coin.Coin import Coin
from sources.eat.Coin.CoinType import CoinType
from sources.eat.Eatable import Eatable
from sources.game_set import *
from sources.images import BulbasaurImage, SquirtleImage, CharmanderImage
from sources.musics import BackgroundMusic


@dataclass
class Game:
    character: Character
    background: Background
    bonus_count: int
    score: int
    time: Time

    def __init__(self):
        self.background = Background(BackgroundImage.default_background, BackgroundMusic.default, screen_width,
                                     screen_height)
        self.time = Time()
        self.score = 0
        self.character = self.choose_character()
        self.bonus_count = 0

    def start_game(self):
        self.background.show_default_screen(screen_width, screen_height)
        self.background.screen.blit(self.character.current_image, (character_x_pos, self.character.y_pos))
        pygame.display.update()

    def bonus_stage(self, background: Background):
        self.background = background

    def choose_character(self) -> Character:
        self.background.screen.fill(pygame.Color("white"))
        self.background.choose_character_screen(self.background.screen)

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
            return Squirtle(SquirtleImage.image_1)
        elif character_type is CharacterType.CHARMANDER:
            return Charmander(CharmanderImage.image_1)
        elif character_type is CharacterType.BULBASAUR:
            return Bulbasaur(BulbasaurImage.image_1)

    def add_score(self, element: Eatable):
        self.score += element.score

    def update_character(self):
        self.character.update_motion()
        self.background.screen.blit(self.character.current_image, (self.character.x_pos, self.character.y_pos))

    def show_bonus_coin(self, objects: [Object]) -> [Object]:
        is_bonus = True if int(random.randrange(0, 4)) == 1 else False

        if is_bonus:
            if self.bonus_count == 0:
                letter = Bonus(BonusCoin.B)
                objects.append(letter)
                self.bonus_count += 1
                self.background.screen.blit(letter.image, (screen_width - letter.image.get_width(), letter.y_pos))

            elif self.bonus_count == 1:
                letter = Bonus(BonusCoin.O)
                objects.append(letter)
                self.bonus_count += 1
                self.background.screen.blit(letter.image, (screen_width - letter.image.get_width(), letter.y_pos))

            elif self.bonus_count == 2:
                letter = Bonus(BonusCoin.N)
                objects.append(letter)
                self.bonus_count += 1
                self.background.screen.blit(letter.image, (screen_width - letter.image.get_width(), letter.y_pos))

            elif self.bonus_count == 3:
                letter = Bonus(BonusCoin.U)
                objects.append(letter)
                self.bonus_count += 1
                self.background.screen.blit(letter.image, (screen_width - letter.image.get_width(), letter.y_pos))

            elif self.bonus_count == 4:
                letter = Bonus(BonusCoin.S)
                objects.append(letter)
                self.bonus_count += 1
                self.background.screen.blit(letter.image, (screen_width - letter.image.get_width(), letter.y_pos))

        else:
            coin = Coin(CoinType.BRONZE)
            objects.append(coin)
            self.background.screen.blit(coin.image, (screen_width - coin.image.get_width(), coin.y_pos))

        return objects
