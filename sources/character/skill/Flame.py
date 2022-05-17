import pygame

from sources.character.skill.Skill import Skill
from sources.character.skill.Type import SkillType
from sources.images import Charmander


class Flame(Skill):

    def __init__(self):
        super().__init__(Charmander.charmander_skill_1)

        self.type = SkillType.TIME
        self.image1 = Charmander.charmander_skill_1
        self.image2 = Charmander.charmander_skill_2
        self.time = 5
        self.delay = 10

    def get_width(self) -> int:
        return self.current_image.get_width()

    def get_height(self) -> int:
        return self.current_image.get_height()

# TODO 불에 맞춰서 width, height 리턴해야함