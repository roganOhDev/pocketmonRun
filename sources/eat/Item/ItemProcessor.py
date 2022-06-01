from dataclasses import dataclass

from sources.eat.Item.ItemType import ItemType


@dataclass
class ItemProcessor:
    item_start_time: float
    item_type: ItemType
    is_invincibility: bool = False
    item_time: int = 5

