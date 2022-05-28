import time
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
from sources.game_set import *
from sources.musics import CharacterMusic

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
    slide_images: [Surface]
    slide_bgm: Sound
    jump_bgm: Sound
    bonus_status: BonusStatus

    skill: Skill

    def __init__(self, skill: Skill):
        self.x_pos = character_x_pos
        self.current_image = self.image1
        self.current_image_bool = True
        self.status = CharacterStatus.RUNNING
        self.y_pos = screen_height - floor_height - self.get_height() + self.fix_y_value()
        self.bonus_status = BonusStatus(False, False, False, False, False)
        self.y_speed = 0
        self.life = 100
        self.motion_count = 0
        self.slide_bgm = pygame.mixer.Sound(CharacterMusic.slide)
        self.jump_bgm = pygame.mixer.Sound(CharacterMusic.jump)

        if isinstance(skill, Health):
            self.life *= Health().health_multiply

    def get_width(self) -> float:
        return self.current_image.get_width()

    def get_height(self) -> float:
        return self.current_image.get_height()

    def fix_y_value(self) -> int:
        if self.type is CharacterType.CHARMANDER:
            if self.status is CharacterStatus.SLIDING:
                return 51
            return 21

        elif self.type is CharacterType.BULBASAUR:
            if self.status is CharacterStatus.SLIDING:
                return 39
            return 9

        elif self.type is CharacterType.SQUIRTLE:
            if self.status is CharacterStatus.SLIDING:
                return 52
            return 22

    def reduce_life(self):
        self.life -= 1 / fps

    def is_life_remain(self) -> bool:
        return self.life > 0

    def update_motion(self):
        if self.status is CharacterStatus.RUNNING:
            if self.motion_count >= 10:
                self.current_image = self.image1 if self.current_image_bool else self.image2
                self.current_image_bool = not self.current_image_bool

            self.motion_count = (self.motion_count + 1) % 11

        elif self.is_jumping():
            self.jumping()

        elif self.status is CharacterStatus.SLIDING:
            if self.motion_count >= 7:
                self.current_image \
                    = self.slide_images[self.choose_slide_image_index(0 if self.current_image_bool else 1)]
                self.current_image_bool = not self.current_image_bool

            self.motion_count = (self.motion_count + 1) % 8

    def skill_process(self):
        if self.skill.type is SkillType.PASSIVE:
            return

        else:
            if (not self.skill.is_using) and time.time() - self.skill.skill_end_time >= self.skill.delay:
                self.start_using_skill()

            elif self.skill.is_using and time.time() - self.skill.skill_start_time < self.skill.time:
                self.keep_using_skill()

            elif self.skill.is_using and time.time() - self.skill.skill_start_time >= self.skill.time:
                self.stop_using_skill()

    def start_using_skill(self):
        if self.status is CharacterStatus.SLIDING:
            self.slide_bgm.stop()
            self.status = CharacterStatus.RUNNING
            self.y_pos = screen_height - floor_height - self.get_height() + self.fix_y_value()

        self.skill.is_using = True
        self.skill.update_motion()
        self.current_image = self.skill.current_image
        self.skill.skill_start_time = time.time()

    def keep_using_skill(self):
        self.skill.update_motion()
        self.current_image = self.skill.current_image

    def stop_using_skill(self):
        self.skill.is_using = False
        self.skill.skill_end_time = time.time()
        self.current_image = self.image1

    def choose_slide_image_index(self, num: int) -> int:
        return (len(self.slide_images) - 1) * num

    def y_move(self, y_pos: float):
        self.y_pos = y_pos

    def is_jumping(self) -> bool:
        return self.status in (CharacterStatus.DOUBLE_JUMPING, CharacterStatus.JUMPING)

    def run(self):
        self.slide_bgm.stop()
        self.jump_bgm.stop()

        self.status = CharacterStatus.RUNNING
        self.current_image = self.image2
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
                self.current_image = self.skill.images[0]
            else:
                self.current_image = self.image1

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

            if not self.skill.is_using:
                self.slide_bgm.play()
                self.status = CharacterStatus.SLIDING
                self.current_image = self.slide_images[0]
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
