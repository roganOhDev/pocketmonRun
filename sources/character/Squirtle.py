from sources.character.Character import Character, CharacterType
from sources.character.skill.Flame import Flame
from sources.character.skill.Shield import Shield
from sources.images import Squirtle


class Squirtle(Character):

    def __init__(self, image_path):
        skill = Shield()
        super().__init__(image_path, skill)

        self.type = CharacterType.SQUIRTLE
        self.image1 = Squirtle.image1
        self.image2 = Squirtle.image2
        self.skill = skill
