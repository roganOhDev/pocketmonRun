import random
from dataclasses import dataclass

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
from sources.images import BulbasaurImage, SquirtleImage, CharmanderImage, BonusImage
from sources.musics import BackgroundMusic, CoinMusic


@dataclass
class Game:
    character: Character
    background: Background
    bonus_count: int
    bonus_eat_count: int
    score: int
    time: Time
    is_default_background: bool

    def __init__(self):
        self.background = Background(BackgroundImage.default_background, BackgroundMusic.default, screen_width,
                                     screen_height)
        self.time = Time()
        self.score = 0
        self.character = self.choose_character()
        self.bonus_count = 0
        self.bonus_eat_count = 0
        self.is_default_background = True

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
                self.__show_bonus_coin(objects, BonusCoin.B)
            elif self.bonus_count == 1:
                self.__show_bonus_coin(objects, BonusCoin.O)
            elif self.bonus_count == 2:
                self.__show_bonus_coin(objects, BonusCoin.N)
            elif self.bonus_count == 3:
                self.__show_bonus_coin(objects, BonusCoin.U)
            elif self.bonus_count == 4:
                self.__show_bonus_coin(objects, BonusCoin.S)

        else:
            coin = Coin(CoinType.BRONZE)
            objects.append(coin)
            self.background.screen.blit(coin.image, (screen_width - coin.image.get_width(), coin.y_pos))

        return objects

    def process_collision(self, objects: [Object]) -> None:
        for index, object in enumerate(objects):
            if self.__is_collision(object):
                if isinstance(object, Coin) and self.is_default_background:
                    eat_bgm = pygame.mixer.Sound(CoinMusic.default)
                    eat_bgm.play()
                    self.score += object.score

                elif isinstance(object, Coin) and not self.is_default_background:
                    eat_bgm = pygame.mixer.Sound(CoinMusic.bonus)
                    eat_bgm.play()
                    self.score += object.score

                if isinstance(object, Bonus):
                    eat_bgm = pygame.mixer.Sound(CoinMusic.default)
                    eat_bgm.play()
                    self.bonus_eat_count += 1
                    self.score += object.score

                objects.pop(index)

    def __is_collision(self, object: Object) -> bool:
        if self.character.x_pos <= object.x_pos <= self.character.x_pos + self.character.get_width() and \
                self.character.y_pos <= object.y_pos <= self.character.y_pos + self.character.get_height():
            return True
        else:
            return False

    def show_current_bonus_collection(self) -> None:
        if self.bonus_eat_count == 0:
            B = pygame.image.load(BonusImage.B_transparency).convert()
            B = pygame.transform.rotozoom(B, 0, 0.2)
            O = pygame.image.load(BonusImage.O_transparency).convert()
            O = pygame.transform.rotozoom(O, 0, 0.2)
            N = pygame.image.load(BonusImage.N_transparency).convert()
            N = pygame.transform.rotozoom(N, 0, 0.2)
            U = pygame.image.load(BonusImage.U_transparency).convert()
            U = pygame.transform.rotozoom(U, 0, 0.2)
            S = pygame.image.load(BonusImage.S_transparency).convert()
            S = pygame.transform.rotozoom(S, 0, 0.2)

        elif self.bonus_eat_count == 1:
            B = pygame.image.load(BonusImage.B).convert()
            B = pygame.transform.rotozoom(B, 0, 0.2)
            O = pygame.image.load(BonusImage.O_transparency).convert()
            O = pygame.transform.rotozoom(O, 0, 0.2)
            N = pygame.image.load(BonusImage.N_transparency).convert()
            N = pygame.transform.rotozoom(N, 0, 0.2)
            U = pygame.image.load(BonusImage.U_transparency).convert()
            U = pygame.transform.rotozoom(U, 0, 0.2)
            S = pygame.image.load(BonusImage.S_transparency).convert()
            S = pygame.transform.rotozoom(S, 0, 0.2)

        elif self.bonus_eat_count == 2:
            B = pygame.image.load(BonusImage.B).convert()
            B = pygame.transform.rotozoom(B, 0, 0.2)
            O = pygame.image.load(BonusImage.O).convert()
            O = pygame.transform.rotozoom(O, 0, 0.2)
            N = pygame.image.load(BonusImage.N_transparency).convert()
            N = pygame.transform.rotozoom(N, 0, 0.2)
            U = pygame.image.load(BonusImage.U_transparency).convert()
            U = pygame.transform.rotozoom(U, 0, 0.2)
            S = pygame.image.load(BonusImage.S_transparency).convert()
            S = pygame.transform.rotozoom(S, 0, 0.2)

        elif self.bonus_eat_count == 3:
            B = pygame.image.load(BonusImage.B).convert()
            B = pygame.transform.rotozoom(B, 0, 0.2)
            O = pygame.image.load(BonusImage.O).convert()
            O = pygame.transform.rotozoom(O, 0, 0.2)
            N = pygame.image.load(BonusImage.N).convert()
            N = pygame.transform.rotozoom(N, 0, 0.2)
            U = pygame.image.load(BonusImage.U_transparency).convert()
            U = pygame.transform.rotozoom(U, 0, 0.2)
            S = pygame.image.load(BonusImage.S_transparency).convert()
            S = pygame.transform.rotozoom(S, 0, 0.2)

        elif self.bonus_eat_count == 4:
            B = pygame.image.load(BonusImage.B).convert()
            B = pygame.transform.rotozoom(B, 0, 0.2)
            O = pygame.image.load(BonusImage.O).convert()
            O = pygame.transform.rotozoom(O, 0, 0.2)
            N = pygame.image.load(BonusImage.N).convert()
            N = pygame.transform.rotozoom(N, 0, 0.2)
            U = pygame.image.load(BonusImage.U).convert()
            U = pygame.transform.rotozoom(U, 0, 0.2)
            S = pygame.image.load(BonusImage.S_transparency).convert()
            S = pygame.transform.rotozoom(S, 0, 0.2)

        elif self.bonus_eat_count == 5:
            B = pygame.image.load(BonusImage.B).convert()
            B = pygame.transform.rotozoom(B, 0, 0.2)
            O = pygame.image.load(BonusImage.O).convert()
            O = pygame.transform.rotozoom(O, 0, 0.2)
            N = pygame.image.load(BonusImage.N).convert()
            N = pygame.transform.rotozoom(N, 0, 0.2)
            U = pygame.image.load(BonusImage.U).convert()
            U = pygame.transform.rotozoom(U, 0, 0.2)
            S = pygame.image.load(BonusImage.S).convert()
            S = pygame.transform.rotozoom(S, 0, 0.2)

        self.background.screen.blit(B, (200, 15))
        self.background.screen.blit(O, (230, 15))
        self.background.screen.blit(N, (260, 15))
        self.background.screen.blit(U, (290, 15))
        self.background.screen.blit(S, (320, 15))

    def __show_bonus_coin(self,objects: [Object], bonus_coin: BonusCoin):
        letter = Bonus(bonus_coin)
        objects.append(letter)
        self.bonus_count += 1
        self.background.screen.blit(letter.image, (screen_width - letter.image.get_width(), letter.y_pos))
