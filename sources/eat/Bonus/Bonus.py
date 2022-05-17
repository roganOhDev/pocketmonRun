from sources.eat.Bonus.BonusCoin import BonusCoin
from sources.eat.Coin.CoinType import CoinType
from sources.eat.Eatable import Eatable
from sources.images import BonusImage


class Bonus(Eatable):
    type: BonusCoin

    def __init__(self, type: BonusCoin):
        image_path = self.get_image_path(type)
        super().__init__(image_path)

        self.score = CoinType.BRONZE.value
        self.type = type

    @staticmethod
    def get_image_path(type: BonusCoin) -> str:
        if type is BonusCoin.B:
            return BonusImage.B
        elif type is BonusCoin.O:
            return BonusImage.O
        elif type is BonusCoin.N:
            return BonusImage.N
        elif type is BonusCoin.U:
            return BonusImage.U
        elif type is BonusCoin.S:
            return BonusImage.S
