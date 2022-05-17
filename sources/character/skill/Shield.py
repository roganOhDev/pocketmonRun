import pygame

from sources.character.skill.Skill import Skill
from sources.character.skill.Type import SkillType
from sources.images import Squirtle


class Shield(Skill):

    def __init__(self):
        super().__init__(Squirtle.squirtle_skill_1)

        self.type = SkillType.TIME
        self.image1 = Squirtle.squirtle_skill_1
        self.image2 = Squirtle.squirtle_skill_2
        self.time = 5
        self.delay = 10