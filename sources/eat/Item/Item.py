from sources.eat.Coin.CoinType import CoinType
from sources.eat.Eatable import Eatable
from sources.eat.Item.ItemType import ItemType
from sources.images import ItemImage


class Item(Eatable):
    type: ItemType

    def __init__(self, type: ItemType):
        image_path = self.get_image_path(type)
        super().__init__(image_path)

        self.score = CoinType.BRONZE.value
        self.type = type

    @staticmethod
    def get_image_path(type: ItemType) -> str:
        if type is ItemType.GIANT:
            return ItemImage.giant
        elif type is ItemType.BOOST:
            return ItemImage.boost
        elif type is ItemType.REVIVE:
            return ItemImage.revive
        elif type is ItemType.HEALTH:
            return ItemImage.health