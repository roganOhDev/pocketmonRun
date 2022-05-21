import pygame

from sources.character.Character import Character, CharacterType
from sources.character.skill.Health import Health
from sources.images import BulbasaurImage


class Bulbasaur(Character):

    def __init__(self, image1_path):
        skill = Health()
        super().__init__(image1_path, skill)

        self.type = CharacterType.BULBASAUR
        self.image1 = pygame.image.load(BulbasaurImage.image_1)
        self.image2 = pygame.image.load(BulbasaurImage.image_2)
        self.skill = skill
