import pygame

from sources.character.Character import Character, CharacterType
from sources.character.skill.Flame import Flame
from sources.images import CharmanderImage

y_fix: float = 30
class Charmander(Character):

    def __init__(self, image1_path):
        skill = Flame()

        self.type = CharacterType.CHARMANDER

        image1 = pygame.image.load(CharmanderImage.image_1).convert_alpha()
        self.image1 = pygame.transform.rotozoom(image1, 0, 0.7)
        image2 = pygame.image.load(CharmanderImage.image_2).convert_alpha()
        self.image2 = pygame.transform.rotozoom(image2, 0, 0.7)

        self.skill = skill

        self.slide_images = []
        slide_image_1 = pygame.image.load(CharmanderImage.slide_1).convert_alpha()
        self.slide_images.append(pygame.transform.rotozoom(slide_image_1, 0, 0.8))
        # slide_image_2 = pygame.image.load(CharmanderImage.slide_2).convert_alpha()
        # self.slide_images.append(pygame.transform.rotozoom(slide_image_2, 0, 0.8))

        super().__init__(skill)
