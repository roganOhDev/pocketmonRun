from sources.character.skill.Skill import Skill
from sources.character.skill.Type import SkillType


class Health(Skill):
    health_multiply: float = 1.3

    def __init__(self):
        super().__init__("", 0)
        self.type = SkillType.PASSIVE

    @staticmethod
    def get_health_mutiply() -> float:
        return 1.3
