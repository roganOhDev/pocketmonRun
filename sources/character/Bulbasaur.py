from pygame.surface import Surface

from sources.character.Character import Character, CharacterType
from sources.character.skill.Health import Health
from sources.images import Bulbasaur


class Bulbasaur(Character):

    def __init__(self, image_path):
        skill = Health()
        super().__init__(image_path, skill)

        self.type = CharacterType.BULBASAUR
        self.image1 = Bulbasaur.bulbasaur_1
        self.image2 = Bulbasaur.bulbasaur_2
        self.skill = skill
