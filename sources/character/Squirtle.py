from sources.character.Character import Character, CharacterType
from sources.character.skill.Flame import Flame
from sources.character.skill.Shield import Shield
from sources.images import SquirtleImage


class Squirtle(Character):

    def __init__(self, image1_path):
        skill = Shield()
        super().__init__(image1_path, skill)

        self.type = CharacterType.SQUIRTLE
        self.image1 = SquirtleImage.image1
        self.image2 = SquirtleImage.image2
        self.skill = skill
