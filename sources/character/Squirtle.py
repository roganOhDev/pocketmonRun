import pygame

from sources.character.Character import Character, CharacterType
from sources.character.skill.Shield import Shield
from sources.images import SquirtleImage

y_fix: float = 45

class Squirtle(Character):

    def __init__(self, image1_path):
        skill = Shield()

        self.type = CharacterType.SQUIRTLE

        image1 = pygame.image.load(SquirtleImage.image_1).convert()
        self.image1 = pygame.transform.rotozoom(image1, 0, 0.5)
        image2 = pygame.image.load(SquirtleImage.image_2).convert()
        self.image2 = pygame.transform.rotozoom(image2, 0, 0.5)

        self.skill = skill

        self.slide_images = []
        slide_image = pygame.image.load(SquirtleImage.slide).convert()
        self.slide_images.append(pygame.transform.rotozoom(slide_image, 0, 0.8))

        super().__init__(skill)

