from sources.character.skill.Skill import Skill
from sources.character.skill.Type import SkillType
from sources.images import CharmanderImage


class Flame(Skill):

    def __init__(self):
        super().__init__(CharmanderImage.skill_1)

        self.type = SkillType.TIME
        self.image1 = CharmanderImage.skill_1
        self.image2 = CharmanderImage.skill_2
        self.time = 5
        self.delay = 10

    def get_width(self) -> int:
        return self.current_image.get_width()

    def get_height(self) -> int:
        return self.current_image.get_height()

# TODO 불에 맞춰서 width, height 리턴해야함
