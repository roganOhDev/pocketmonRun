import pygame

from sources.character.skill.Skill import Skill
from sources.character.skill.Type import SkillType


class Health(Skill):
    health_multiply: 1.3

    def __init__(self):
        super().__init__("")
        self.type = SkillType.PASSIVE
