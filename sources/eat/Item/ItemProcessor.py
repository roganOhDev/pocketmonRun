from dataclasses import dataclass

from sources.eat.Item.ItemType import ItemType


@dataclass
class ItemProcessor:
    item_type: ItemType
    item_start_time: float = 0
    item_time: int = 3
    is_active: bool = False

