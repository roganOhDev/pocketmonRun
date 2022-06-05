import random
from dataclasses import dataclass

import pygame.display

from sources.character.BonusStatus import BonusStatus
from sources.character.Bulbasaur import Bulbasaur
from sources.character.Character import Character, CharacterType
from sources.character.Character import character_x_pos
from sources.character.Charmander import Charmander
from sources.character.Squirtle import Squirtle
from sources.character.skill.Flame import Flame
from sources.character.skill.Health import Health
from sources.character.skill.Shield import Shield
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
from sources.eat.Item.Item import Item
from sources.eat.Item.ItemType import ItemType
from sources.game_set import *
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

    def __init__(self, game_time: float):
        self.background = Background(BackgroundImage.default_background, BackgroundMusic.default)
        self.time = Time()
        self.score = 0
        self.character = self.choose_character(game_time)
        self.is_default_stage = True

    def start_game(self):
        self.background.show_default_screen()
        self.background.screen.blit(self.character.current_image, (character_x_pos, self.character.y_pos))

    def bonus_stage(self, background: Background):
        self.background = background

    def choose_character(self, game_time: float) -> Character:
        self.background.screen.fill(pygame.Color("white"))
        self.background.choose_character_screen(self.background.screen)

        while True:
            for event in (pygame.event.get()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 < event.pos[0] < screen_width / 2 and 0 < event.pos[1] < screen_height / 2:
                        return self.create_character(CharacterType.CHARMANDER, game_time)

                    elif 0 < event.pos[0] < screen_width / 2 and screen_height / 2 < event.pos[1] < screen_height:
                        return self.create_character(CharacterType.BULBASAUR, game_time)

                    elif screen_width / 2 < event.pos[0] < screen_width and \
                            screen_height / 2 < event.pos[1] < screen_height:
                        return self.create_character(CharacterType.SQUIRTLE, game_time)

    @staticmethod
    def create_character(character_type: CharacterType, game_time: float):
        if character_type is CharacterType.SQUIRTLE:
            return Squirtle(game_time)
        elif character_type is CharacterType.CHARMANDER:
            return Charmander(game_time)
        elif character_type is CharacterType.BULBASAUR:
            return Bulbasaur()

    def add_score(self, element: Eatable):
        self.score += element.score

    def update_character(self, game_time: float):
        self.character.update_motion()
        self.character.skill_process(game_time)
        self.character.reduce_life()
        self.character.item_process(game_time)
        self.background.screen.blit(self.character.current_image, (self.character.x_pos, self.character.y_pos))

    def show_bonus_coin(self, objects: [Object]) -> [Object]:
        rand_num = int(random.randrange(0, 5))
        is_bonus = (True if rand_num <= 3 else False) and (not self.has_bonus_coin(objects))

        if is_bonus:
            self.__show_bonus_coin(objects, self.character.bonus_status.choose_bonus_coin())

        elif rand_num == 4:
            self.__show_specific_item(objects, ItemType.HEALTH)

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

    def process_collision(self, objects: [Object]) -> None:
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
                    if self.character.skill.is_using and self.__is_collision_with_skill(object, upside_down):
                        if isinstance(self.character.skill, Flame):
                            self.score += CoinType.GOLD.value

                    elif not self.character.item_processors:
                        self.character.life -= 20
                    objects.pop(index)

                elif isinstance(object, Item):
                    if object.type is ItemType.HEALTH:
                        self.__eat_health_item()
                        objects.pop(index)

                    elif object.type is ItemType.BOOST:
                        self.character.eat_boost_item()
                        objects.pop(index)

                    elif object.type is ItemType.GIANT:
                        self.character.eat_giant_item()
                        objects.pop(index)

    def __eat_health_item(self):
        self.character.life = self.character.max_life if self.character.life + 30 > self.character.max_life else self.character.life + 30

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
            character_high += 18

        elif self.character.type is CharacterType.SQUIRTLE and not isinstance(object, Trap):
            character_high += 3

        elif self.character.type is CharacterType.BULBASAUR and not isinstance(object, Trap):
            character_high -= 5

        if self.character.type is CharacterType.BULBASAUR and isinstance(object, Item):
            character_high -= 4

        if isinstance(object, Item):
            if object.type is ItemType.BOOST:
                object_high += 7

        if not isinstance(object, Trap):
            if (character_left <= object_left <= character_right) and (
                    character_high <= object_high <= character_low):
                    # print("item type: " + str(object.type))
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

    def __is_collision_with_skill(self, object: Object, upside_down: bool) -> bool:
        skill_right = self.character.x_pos + self.character.get_width()
        skill_left = skill_right - self.character.skill.get_width()
        skill_low = self.character.y_pos + self.character.get_height() - 10
        skill_high = self.character.y_pos + 10

        object_left = object.x_pos
        object_right = object.x_pos + object.image.get_width()
        object_high = object.y_pos
        object_low = object.y_pos + object.image.get_height()

        if isinstance(self.character.skill, Shield):
            return True

        elif upside_down and (
                skill_left + 60 <= object_right) and (
                object_left <= skill_right - 40) and (
                skill_high + 15 <= object_low):
            # print("obstacle_low:  " + str(object_low))
            # print("character_high:  " + str(character_high))
            return True

        elif not upside_down and (
                skill_left + 60 <= object_right) and (
                object_left <= skill_right - 25) and (
                skill_low - 15 >= object_high):
            return True

        return False

    def __show_bonus_coin(self, objects: [Object], bonus_coin: BonusCoinType) -> None:
        if bonus_coin is BonusCoinType.FULL:
            return

        letter = Bonus(bonus_coin)
        objects.append(letter)
        self.background.screen.blit(letter.image, (screen_width, letter.y_pos))

    def show_item(self, objects: [Object]) -> None:
        rand_num = int(random.randrange(0, 10))
        if rand_num in (0, 1, 2, 3, 4, 5, 6, 7):
            coin = Coin(CoinType.SILVER, 0)
            objects.append(coin)
            self.background.screen.blit(coin.image, (screen_width - coin.image.get_width(), coin.y_pos))

        elif rand_num == 8:
            self.__show_specific_item(objects, ItemType.BOOST)
        elif rand_num == 9:
            self.__show_specific_item(objects, ItemType.GIANT)

    def __show_specific_item(self, objects: [Object], item_type: ItemType):
        item = Item(item_type)
        objects.append(item)
        self.background.screen.blit(item.image, (screen_width, item.y_pos))

    def show_score(self) -> None:
        score_text = Text(40, 30, 20, str(int(self.score)), (255, 255, 0))
        self.background.screen.blit(score_text.render(), score_text.get_pos())

    def show_life(self) -> None:
        full_life = 100 if self.character.skill.type is SkillType.TIME else 100 * Health.get_health_mutiply()
        pygame.draw.rect(self.background.screen, (192, 192, 192), [300, 15, (screen_width / 2) * full_life / 100, 30])

        pygame.draw.rect(self.background.screen, (102, 102, 255),
                         [300, 20, (screen_width / 2) * self.character.life / 100, 20])

    def bonus_process(self, game_time: float, objects: [Object]):
        if self.character.bonus_status.bonus_eat_count == 5:
            self.bonus_stage_start_time = game_time
            self.character.bonus_status.bonus_eat_count = 6
            self.is_default_stage = False
            self.background.show_bonus_screen(objects)

        elif self.character.bonus_status.bonus_eat_count == 6:
            if game_time - self.bonus_stage_start_time >= 15:
                self.character.bonus_status = BonusStatus(False, False, False, False, False)
                self.character.bonus_status.bonus_eat_count = 0
                self.background.show_default_screen()
                self.is_default_stage = True
