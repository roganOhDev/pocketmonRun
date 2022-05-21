import pygame

from sources.character.Character import Character, CharacterType
from sources.character.skill.Health import Health
from sources.images import BulbasaurImage

y_fix: float = 17

class Bulbasaur(Character):

    def __init__(self, image1_path):
        skill = Health()

        self.type = CharacterType.BULBASAUR
        self.image1 = pygame.image.load(BulbasaurImage.image_1)
        self.image2 = pygame.image.load(BulbasaurImage.image_2)
        self.skill = skill

        super().__init__(image1_path, skill)
