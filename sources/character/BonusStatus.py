from dataclasses import dataclass

from pygame import Surface

from sources.common.Text import Text
from sources.eat.Bonus.BonusCoinType import BonusCoinType


@dataclass
class BonusStatus:
    B: bool
    O: bool
    N: bool
    U: bool
    S: bool

    bonus_eat_count: int = 0
    size: int = 30
    y_pos: int = 20

    def choose_bonus_coin(self) -> BonusCoinType:
        if not self.B:
            return BonusCoinType.B
        elif not self.O:
            return BonusCoinType.O
        elif not self.N:
            return BonusCoinType.N
        elif not self.U:
            return BonusCoinType.U
        elif not self.S:
            return BonusCoinType.S
        else:
            return BonusCoinType.FULL

    def eat_bonus_coin(self, type: BonusCoinType) -> None:
        if type is BonusCoinType.B:
            self.bonus_eat_count += 1
            self.B = True
        if type is BonusCoinType.O:
            self.bonus_eat_count += 1
            self.O = True
        if type is BonusCoinType.N:
            self.bonus_eat_count += 1
            self.N = True
        if type is BonusCoinType.U:
            self.bonus_eat_count += 1
            self.U = True
        if type is BonusCoinType.S:
            self.bonus_eat_count += 1
            self.S = True

    def show_current_bonus_collection(self, screen: Surface) -> None:
        if self.B:
            b = Text(self.size, 150, self.y_pos, "B", (255, 0, 0))
        else:
            b = Text(self.size, 150, self.y_pos, "B", (108, 108, 108))

        if self.O:
            o = Text(self.size, 180, self.y_pos, "O", (255, 128, 0))
        else:
            o = Text(self.size, 180, self.y_pos, "O", (108, 108, 108))

        if self.N:
            n = Text(self.size, 210, self.y_pos, "N", (255, 255, 0))
        else:
            n = Text(self.size, 210, self.y_pos, "N", (108, 108, 108))

        if self.U:
            u = Text(self.size, 240, self.y_pos, "U", (128, 255, 0))
        else:
            u = Text(self.size, 240, self.y_pos, "U", (108, 108, 108))

        if self.S:
            s = Text(self.size, 270, self.y_pos, "S", (0, 0, 255))
        else:
            s = Text(self.size, 270, self.y_pos, "S", (108, 108, 108))

        screen.blit(b.render(), b.get_pos())
        screen.blit(o.render(), o.get_pos())
        screen.blit(n.render(), n.get_pos())
        screen.blit(u.render(), u.get_pos())
        screen.blit(s.render(), s.get_pos())
