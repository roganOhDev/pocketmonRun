from sources.eat.Bonus.BonusCoinType import BonusCoinType
from sources.eat.Coin.CoinType import CoinType
from sources.eat.Eatable import Eatable
from sources.images import BonusImage


class Bonus(Eatable):
    type: BonusCoinType

    def __init__(self, type: BonusCoinType):
        image_path = self.get_image_path(type)
        super().__init__(image_path, 0)

        self.score = CoinType.BRONZE.value
        self.type = type

    @staticmethod
    def get_image_path(type: BonusCoinType) -> str:
        if type is BonusCoinType.B:
            return BonusImage.B
        elif type is BonusCoinType.O:
            return BonusImage.O
        elif type is BonusCoinType.N:
            return BonusImage.N
        elif type is BonusCoinType.U:
            return BonusImage.U
        elif type is BonusCoinType.S:
            return BonusImage.S
