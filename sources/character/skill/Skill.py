import time
from dataclasses import dataclass

from pygame.surface import Surface

from sources.character.skill.Type import SkillType


@dataclass
class Skill:
    images: [Surface]
    width: float
    height: float
    type: SkillType
    time: int
    delay: int
    current_image: Surface
    image_none_change_count: int
    image_num: int
    is_using: bool

    skill_end_time: float
    skill_start_time: float = 0

    def __init__(self, images: [Surface]):
        self.is_using = False
        if images:
            self.images = images
            self.current_image = self.images[0]
            self.image_none_change_count = 0
            self.image_num = 0
            self.skill_end_time = time.time()

    def get_width(self):
        return self.current_image.get_width()

    def get_height(self):
        return self.current_image.get_height()

    def update_motion(self):
        if self.image_none_change_count >= 10:
            self.current_image = self.images[self.image_num]
            self.image_num = (self.image_num + 1) % len(self.images)
            self.image_none_change_count = 0

        else:
            self.image_none_change_count += 1