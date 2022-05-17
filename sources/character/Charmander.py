from sources.character.Character import Character, CharacterType
from sources.character.skill.Flame import Flame
from sources.images import Charmander


class Charmander(Character):

    def __init__(self, image_path):
        skill = Flame()
        super().__init__(image_path, skill)

        self.type = CharacterType.CHARMANDER
        self.image1 = Charmander.image1
        self.image2 = Charmander.image2
        self.skill = skill
