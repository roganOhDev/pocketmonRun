from sources.character.Character import Character, CharacterType
from sources.character.skill.Flame import Flame
from sources.images import CharmanderImage


class Charmander(Character):

    def __init__(self, image1_path):
        skill = Flame()
        super().__init__(image1_path, skill)

        self.type = CharacterType.CHARMANDER
        self.image1 = CharmanderImage.image1
        self.image2 = CharmanderImage.image2
        self.skill = skill
