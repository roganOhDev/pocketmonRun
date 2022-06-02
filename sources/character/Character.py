from dataclasses import dataclass
from enum import Enum

import pygame.mixer
from pygame import Surface
from pygame.event import Event
from pygame.mixer import Sound

from sources.character.BonusStatus import BonusStatus
from sources.character.CharacterStatus import CharacterStatus
from sources.character.skill.Health import Health
from sources.character.skill.Skill import Skill
from sources.character.skill.Type import SkillType
from sources.eat.Item.ItemProcessor import ItemProcessor
from sources.eat.Item.ItemType import ItemType
from sources.game_set import *
from sources.musics import CharacterMusic, CoinMusic

character_x_pos = 3


class CharacterType(Enum):
    CHARMANDER = 1
    SQUIRTLE = 2
    BULBASAUR = 3


@dataclass
class Character:
    type: CharacterType
    status: CharacterStatus
    current_image: Surface
    current_image_bool: bool
    image1: Surface
    image2: Surface
    life: float
    x_pos: float
    y_pos: float
    y_speed: float
    motion_count: int
    slide_image: Surface
    slide_bgm: Sound
    jump_bgm: Sound
    bonus_status: BonusStatus
    item_processors: [ItemProcessor]

    skill: Skill

    def __init__(self, skill: Skill):
        self.x_pos = character_x_pos
        self.current_image = self.image1
        self.current_image_bool = True
        self.status = CharacterStatus.RUNNING
        self.item_processors = []
        self.y_pos = screen_height - floor_height - self.get_height() + self.fix_y_value()
        self.bonus_status = BonusStatus(False, False, False, False, False)
        self.y_speed = 0
        self.life = 100
        self.max_life = 100
        self.motion_count = 0
        self.slide_bgm = pygame.mixer.Sound(CharacterMusic.slide)
        self.jump_bgm = pygame.mixer.Sound(CharacterMusic.jump)

        if isinstance(skill, Health):
            self.life *= Health().health_multiply
            self.max_life *= Health().health_multiply

    def get_width(self) -> float:
        return self.current_image.get_width()

    def get_height(self) -> float:
        return self.current_image.get_height()

    def set_current_image(self, current_image: Surface):
        for (index, item_process) in enumerate(self.item_processors):
            if item_process.item_type == ItemType.GIANT and item_process.is_active:
                current_image = pygame.transform.rotozoom(current_image, 0, 3)

        self.current_image = current_image

    def fix_y_value(self) -> int:
        value = 0
        for item_process in self.item_processors:
            if item_process.item_type == ItemType.GIANT and item_process.is_active:
                if self.type is CharacterType.CHARMANDER:
                    value += 30

        if self.type is CharacterType.CHARMANDER:
            if self.status is CharacterStatus.SLIDING:
                value += 30
            value += 21

        elif self.type is CharacterType.BULBASAUR:
            if self.status is CharacterStatus.SLIDING:
                value += 30
            value += 9

        elif self.type is CharacterType.SQUIRTLE:
            if self.status is CharacterStatus.SLIDING:
                value += 30
            value += 22

        return value

    def reduce_life(self):
        self.life -= 1 / fps

    def is_life_remain(self) -> bool:
        return self.life > 0

    def update_motion(self):
        if self.status is CharacterStatus.RUNNING:
            if self.motion_count >= 10:
                self.set_current_image(self.image1 if self.current_image_bool else self.image2)
                self.current_image_bool = not self.current_image_bool

            self.motion_count = (self.motion_count + 1) % 11

        elif self.is_jumping():
            self.jumping()

        elif self.status is CharacterStatus.SLIDING:
            if self.skill.is_using:
                self.set_current_image(self.skill.slide_image)
            else:
                self.set_current_image(self.slide_image)

    def skill_process(self, game_time: float):
        if self.skill.type is SkillType.PASSIVE:
            return

        else:
            if (not self.skill.is_using) and game_time - self.skill.skill_end_time >= self.skill.delay:
                self.start_using_skill(game_time)

            elif self.skill.is_using and game_time - self.skill.skill_start_time < self.skill.time:
                self.keep_using_skill()

            elif self.skill.is_using and game_time - self.skill.skill_start_time >= self.skill.time:
                self.stop_using_skill(game_time)

    def start_using_skill(self, game_time: float):
        self.skill.is_using = True
        self.skill.update_motion(self.status == CharacterStatus.SLIDING)
        self.skill.skill_start_time = game_time

    def keep_using_skill(self):
        self.skill.update_motion(self.status == CharacterStatus.SLIDING)
        self.set_current_image(self.skill.current_image)

    def stop_using_skill(self, game_time: float):
        self.skill.is_using = False
        self.skill.skill_end_time = game_time
        self.set_current_image(self.image1)

    def item_process(self, game_time: float):
        for (index, item_process) in enumerate(self.item_processors):
            if item_process.item_type == ItemType.GIANT:
                if not item_process.is_active:
                    self.start_giant_item(game_time, index)

                elif game_time - item_process.item_start_time >= item_process.item_time:
                    self.end_giant_item(index)

    def eat_giant_item(self):
        pygame.mixer.Sound(CoinMusic.default).play()

        for (index, item_process) in enumerate(self.item_processors):
            if item_process.item_type == ItemType.GIANT:
                self.overlap_giant_item(index)
                return

        self.item_processors.append(ItemProcessor(ItemType.GIANT))

    def start_giant_item(self, game_time: float, index: int):
        self.item_processors[index].is_active = True
        self.set_current_image(self.current_image)
        self.y_pos = screen_height - floor_height - self.get_height() + self.fix_y_value()
        self.item_processors[index].item_start_time = game_time

    def overlap_giant_item(self, index):
        self.item_processors[index].item_time += 5

    def end_giant_item(self, index: int):
        self.item_processors[index].is_active = False
        self.set_current_image(pygame.transform.rotozoom(self.current_image, 0, 1 / 3))
        self.y_pos = screen_height - floor_height - self.get_height() + self.fix_y_value()
        self.item_processors.pop(index)

    def eat_boost_item(self):
        pygame.mixer.Sound(CoinMusic.default).play()

        for (index, item_process) in enumerate(self.item_processors):
            if item_process.item_type == ItemType.BOOST:
                self.overlap_boost_item(index)
                return

        self.item_processors.append(ItemProcessor(ItemType.BOOST))

    def start_boost_item(self, game_time: float, index: int):
        self.item_processors[index].item_start_time = game_time
        self.item_processors[index].is_active = True

    def overlap_boost_item(self, index):
        self.item_processors[index].item_time += 5

    def end_boost_item(self, index: int):
        self.item_processors[index].is_active = False
        self.item_processors.pop(index)


    @staticmethod
    def is_giant_item(item_processor: ItemProcessor):
        return item_processor.item_type == ItemType.GIANT

    def y_move(self, y_pos: float):
        self.y_pos = y_pos

    def is_jumping(self) -> bool:
        return self.status in (CharacterStatus.DOUBLE_JUMPING, CharacterStatus.JUMPING)

    def run(self):
        self.slide_bgm.stop()
        self.jump_bgm.stop()

        self.status = CharacterStatus.RUNNING
        self.set_current_image(self.image2)
        self.y_pos = screen_height - floor_height - self.get_height() + self.fix_y_value()
        self.y_speed = 0
        self.motion_count = 0

    def jump(self):
        if self.status is not CharacterStatus.DOUBLE_JUMPING:
            self.jump_bgm.play()

            if self.status is CharacterStatus.JUMPING:
                self.status = CharacterStatus.DOUBLE_JUMPING
            else:
                self.y_pos = screen_height - floor_height - self.get_height()
                self.status = CharacterStatus.JUMPING

            if self.skill.is_using:
                self.set_current_image(self.skill.images[0])
            else:
                self.set_current_image(self.image1)

            self.y_speed = -15
            self.motion_count = 0

    def jumping(self):
        if -15 <= self.y_speed <= 45:
            self.y_move(self.y_pos + self.y_speed)
            self.y_speed += 1

        if self.y_pos > screen_height - floor_height - self.get_height() + self.fix_y_value():
            self.run()

    def slide(self):
        if (not self.is_jumping()) or (
                self.is_jumping() and self.y_pos > screen_height - floor_height - self.get_height() + self.fix_y_value() - 90 and self.y_speed > 0):

            if self.skill.is_using:
                self.set_current_image(self.skill.slide_image)
            else:
                self.set_current_image(self.slide_image)

            self.slide_bgm.play()
            self.status = CharacterStatus.SLIDING
            self.y_pos = screen_height - floor_height - self.get_height() + self.fix_y_value()
            self.motion_count = 0

            self.y_speed = 0

    def character_operation(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.jump()
            elif event.key == pygame.K_DOWN:
                self.slide()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN and self.status == CharacterStatus.SLIDING:
                self.run()
