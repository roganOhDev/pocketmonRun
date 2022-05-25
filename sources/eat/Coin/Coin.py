from sources.eat.Coin.CoinType import CoinType
from sources.eat.Eatable import Eatable
from sources.images import CoinImage


class Coin(Eatable):
    type: CoinType

    def __init__(self, type: CoinType, y_fix: float):
        image_path = self.__get_image_path(type)
        super().__init__(image_path, y_fix)

        self.score = self.__get_coin_score(type)

        self.type = type

    @staticmethod
    def create_coin_with_y_pos(y_fix: float):
        return Coin(CoinType.BRONZE, y_fix)

    @staticmethod
    def __get_image_path(type: CoinType) -> str:
        if type is CoinType.BRONZE:
            return CoinImage.bronze
        elif type is CoinType.SILVER:
            return CoinImage.silver
        elif type is CoinType.GOLD:
            return CoinImage.gold

    @staticmethod
    def __get_coin_score(type: CoinType) -> int:
        if type is CoinType.BRONZE:
            return CoinType.BRONZE.value
        elif type is CoinType.SILVER:
            return CoinType.SILVER.value
        elif type is CoinType.GOLD:
            return CoinType.GOLD.value
