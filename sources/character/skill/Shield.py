import pygame

from sources.character.skill.Skill import Skill
from sources.character.skill.Type import SkillType
from sources.images import SquirtleImage


class Shield(Skill):

    def __init__(self, game_time: float):
        image1 = pygame.image.load(SquirtleImage.skill_1).convert_alpha()
        image1 = pygame.transform.rotozoom(image1, 0, 0.4)
        image2 = pygame.image.load(SquirtleImage.skill_2).convert_alpha()
        image2 = pygame.transform.rotozoom(image2, 0, 0.4)
        slide_image = pygame.image.load(SquirtleImage.slide_skill).convert_alpha()
        slide_image = pygame.transform.rotozoom(slide_image, 0, 0.4)

        images = [image1, image2]

        super().__init__(images, game_time)

        self.type = SkillType.TIME
        self.slide_image = slide_image
        self.time = 2
        self.delay = 10
