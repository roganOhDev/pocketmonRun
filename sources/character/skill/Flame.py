import pygame

from sources.character.skill.Skill import Skill
from sources.character.skill.Type import SkillType
from sources.images import CharmanderImage


class Flame(Skill):

    def __init__(self, game_time: float):
        image1 = pygame.image.load(CharmanderImage.skill_1).convert_alpha()
        image1 = pygame.transform.rotozoom(image1, 0, 0.7)
        image2 = pygame.image.load(CharmanderImage.skill_2).convert_alpha()
        image2 = pygame.transform.rotozoom(image2, 0, 0.7)
        slide_image = pygame.image.load(CharmanderImage.slide_skill).convert_alpha()
        slide_image = pygame.transform.rotozoom(slide_image, 0, 0.7)

        images = [image1, image2]
        super().__init__(images, game_time)

        self.type = SkillType.TIME
        self.time = 2
        self.delay = 10
        self.slide_image = slide_image

    def get_width(self) -> float:
        return self.current_image.get_width() / 2

    def get_height(self) -> int:
        return self.current_image.get_height()
