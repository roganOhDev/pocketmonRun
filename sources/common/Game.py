import random
import time
from dataclasses import dataclass

import pygame.display

from sources.character.BonusStatus import BonusStatus
from sources.character.Bulbasaur import Bulbasaur
from sources.character.Character import Character, CharacterType
from sources.character.Character import character_x_pos
from sources.character.Charmander import Charmander
from sources.character.Squirtle import Squirtle
from sources.character.skill.Health import Health
from sources.character.skill.Type import SkillType
from sources.common.Background import Background
from sources.common.Object import Object
from sources.common.Text import Text
from sources.common.Time import Time
from sources.eat.Bonus.Bonus import Bonus
from sources.eat.Bonus.BonusCoinType import BonusCoinType
from sources.eat.Coin.Coin import Coin
from sources.eat.Coin.CoinType import CoinType
from sources.eat.Eatable import Eatable
from sources.game_set import *
from sources.images import BulbasaurImage, SquirtleImage, CharmanderImage
from sources.musics import BackgroundMusic, CoinMusic
from sources.trap.SlideObstacle1 import SlideObstacle1
from sources.trap.SlideObstacle2 import SlideObstacle2
from sources.trap.Trap import Trap


@dataclass
class Game:
    character: Character
    background: Background
    score: int
    time: Time
    is_default_stage: bool
    bonus_stage_start_time: float

    def __init__(self):
        self.background = Background(BackgroundImage.default_background, BackgroundMusic.default)
        self.time = Time()
        self.score = 0
        self.character = self.choose_character()
        self.is_default_stage = True

    def start_game(self):
        self.background.show_default_screen()
        self.background.screen.blit(self.character.current_image, (character_x_pos, self.character.y_pos))

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
        self.character.reduce_life()
        self.background.screen.blit(self.character.current_image, (self.character.x_pos, self.character.y_pos))

    def show_bonus_coin(self, objects: [Object]) -> [Object]:
        is_bonus = (True if int(random.randrange(0, 4)) <= 3 else False) and (not self.has_bonus_coin(objects))

        if is_bonus:
            self.__show_bonus_coin(objects, self.character.bonus_status.choose_bonus_coin())

        else:
            coin = Coin(CoinType.BRONZE, 0)
            objects.append(coin)
            self.background.screen.blit(coin.image, (screen_width - coin.image.get_width(), coin.y_pos))

        return objects

    @staticmethod
    def has_bonus_coin(objects: [Object]) -> bool:
        for object in objects:
            if isinstance(object, Bonus):
                return True
        return False

    def process_collision(self, objects: [Object]) -> bool:
        for index, object in enumerate(objects):
            upside_down = False

            if isinstance(object, SlideObstacle1) or isinstance(object, SlideObstacle2):
                upside_down = True

            if self.__is_collision(object, upside_down):
                if isinstance(object, Coin) and self.is_default_stage:
                    eat_bgm = pygame.mixer.Sound(CoinMusic.default)
                    eat_bgm.play()
                    self.score += object.score
                    objects.pop(index)

                elif isinstance(object, Coin) and not self.is_default_stage:
                    if self.is_default_stage:
                        eat_bgm = pygame.mixer.Sound(CoinMusic.default)
                        self.score += object.score
                    else:
                        eat_bgm = pygame.mixer.Sound(CoinMusic.bonus)
                        self.score += object.score * 1.8

                    eat_bgm.play()
                    objects.pop(index)

                elif isinstance(object, Bonus):
                    eat_bgm = pygame.mixer.Sound(CoinMusic.default)
                    eat_bgm.play()
                    self.character.bonus_status.eat_bonus_coin(object.type)
                    objects.pop(index)

                elif isinstance(object, Trap):
                    self.character.life -= 20
                    objects.pop(index)

        return True

    def __is_collision(self, object: Object, upside_down: bool) -> bool:
        character_left = self.character.x_pos
        character_right = self.character.x_pos + self.character.get_width()
        character_high = self.character.y_pos
        character_low = self.character.y_pos + self.character.get_height()

        object_left = object.x_pos
        object_right = object.x_pos + object.image.get_width()
        object_high = object.y_pos
        object_low = object.y_pos + object.image.get_height()

        if self.character.type is CharacterType.SQUIRTLE and isinstance(object, Trap) and upside_down:
            character_high += 20

        elif self.character.type is CharacterType.SQUIRTLE and not isinstance(object, Trap):
            character_high += 3

        elif self.character.type is CharacterType.BULBASAUR and not isinstance(object, Trap):
            character_high -= 5

        if not isinstance(object, Trap):
            if (character_left <= object_left <= character_right) and (
                    character_high <= object_high <= character_low):
                # print("obstacle_high:" + str(object_high))
                # print("character_high:  " + str(character_high))
                # print("character_low:  " + str(character_low))
                return True

        else:

            if upside_down and (
                    character_left + 60 <= object_right) and (
                    object_left <= character_right - 40) and (
                    character_high + 15 <= object_low):
                # print("obstacle_low:  " + str(object_low))
                # print("character_high:  " + str(character_high))
                return True

            elif not upside_down and (
                    character_left + 60 <= object_right) and (
                    object_left <= character_right - 25) and (
                    character_low - 15 >= object_high):
                return True

        return False

    def __show_bonus_coin(self, objects: [Object], bonus_coin: BonusCoinType) -> None:
        if bonus_coin is BonusCoinType.FULL:
            return

        letter = Bonus(bonus_coin)
        objects.append(letter)
        self.background.screen.blit(letter.image, (screen_width - letter.image.get_width(), letter.y_pos))

    def show_score(self) -> None:
        score_text = Text(40, 30, 20, str(int(self.score)), (255, 255, 0))
        self.background.screen.blit(score_text.render(), score_text.get_pos())

    def show_life(self) -> None:
        full_life = 100 if self.character.skill.type is SkillType.TIME else 100 * Health.get_health_mutiply()
        pygame.draw.rect(self.background.screen, (192, 192, 192), [300, 15, (screen_width / 2) * full_life / 100, 30])

        pygame.draw.rect(self.background.screen, (102, 102, 255),
                         [300, 20, (screen_width / 2) * self.character.life / 100, 20])

    def bonus_process(self) -> None:
        if self.character.bonus_status.bonus_eat_count == 5:
            self.bonus_stage_start_time = time.time()
            self.character.bonus_status.bonus_eat_count = 6
            self.is_default_stage = False
            self.background.show_bonus_screen()

        elif self.character.bonus_status.bonus_eat_count == 6:
            if time.time() - self.bonus_stage_start_time >= 15:
                self.character.bonus_status = BonusStatus(False, False, False, False, False)
                self.character.bonus_status.bonus_eat_count = 0
                self.background.show_default_screen()
                self.is_default_stage = True

