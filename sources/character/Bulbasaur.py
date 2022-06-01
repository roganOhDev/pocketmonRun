import pygame

from sources.character.Character import Character, CharacterType
from sources.character.skill.Health import Health
from sources.images import BulbasaurImage

y_fix: float = 17

class Bulbasaur(Character):

    def __init__(self, image1_path):
        skill = Health()

        self.type = CharacterType.BULBASAUR

        image1 = pygame.image.load(BulbasaurImage.image_1).convert_alpha()
        self.image1 = pygame.transform.rotozoom(image1, 0, 0.5)
        image2 = pygame.image.load(BulbasaurImage.image_2).convert_alpha()
        self.image2 = pygame.transform.rotozoom(image2, 0, 0.5)

        self.skill = skill

        self.slide_images = []
        slide_image = pygame.image.load(BulbasaurImage.slide).convert_alpha()
        self.slide_images = pygame.transform.rotozoom(slide_image, 0, 0.25)

        super().__init__(skill)
