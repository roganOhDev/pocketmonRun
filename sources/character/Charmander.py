import pygame

from sources.character.Character import Character, CharacterType
from sources.character.skill.Flame import Flame
from sources.images import CharmanderImage

y_fix: float = 30
class Charmander(Character):

    def __init__(self, image1_path):
        skill = Flame()

        self.type = CharacterType.CHARMANDER
        self.image1 = pygame.image.load(CharmanderImage.image_1)
        self.image2 = pygame.image.load(CharmanderImage.image_2)
        self.skill = skill

        super().__init__(image1_path, skill)
