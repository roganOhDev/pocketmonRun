import pygame

from sources.character.skill.Skill import Skill
from sources.character.skill.Type import SkillType
from sources.images import SquirtleImage


class Shield(Skill):

    def __init__(self):
        super().__init__(SquirtleImage.skill_1)

        self.type = SkillType.TIME
        self.image1 = SquirtleImage.skill_1
        self.image2 = SquirtleImage.skill_2
        self.time = 5
        self.delay = 10