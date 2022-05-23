from dataclasses import dataclass

from pygame import Surface

from sources.common.Text import Text
from sources.eat.Bonus.BonusCoin import BonusCoin


@dataclass
class BonusStatus:
    bonus_count: int
    bonus_eat_count: int
    B: bool
    O: bool
    N: bool
    U: bool
    S: bool

    size: int = 30

    def choose_bonus_coin(self) -> BonusCoin:
        if not self.B:
            return BonusCoin.B
        elif not self.O:
            return BonusCoin.O
        elif not self.N:
            return BonusCoin.N
        elif not self.U:
            return BonusCoin.U
        elif not self.S:
            return BonusCoin.S
        else:
            return BonusCoin.FULL

    def eat_bonus_coin(self, type: BonusCoin) -> None:
        if type is BonusCoin.B:
            self.B = True
        if type is BonusCoin.O:
            self.O = True
        if type is BonusCoin.N:
            self.N = True
        if type is BonusCoin.U:
            self.U = True
        if type is BonusCoin.S:
            self.S = True

    def show_current_bonus_collection(self, screen: Surface) -> None:
        if self.B:
            b = Text(self.size, 200, 15, "B", (255, 0, 0))
        else:
            b = Text(self.size, 200, 15, "B", (108, 108, 108))

        if self.O:
            o = Text(self.size, 230, 15, "O", (255, 128, 0))
        else:
            o = Text(self.size, 230, 15, "O", (108, 108, 108))

        if self.N:
            n = Text(self.size, 260, 15, "N", (255, 255, 0))
        else:
            n = Text(self.size, 260, 15, "N", (108, 108, 108))

        if self.U:
            u = Text(self.size, 290, 15, "U", (128, 255, 0))
        else:
            u = Text(self.size, 290, 15, "U", (108, 108, 108))

        if self.S:
            s = Text(self.size, 320, 15, "S", (0, 0, 255))
        else:
            s = Text(self.size, 320, 15, "S", (108, 108, 108))

        screen.blit(b.render(), b.get_pos())
        screen.blit(o.render(), o.get_pos())
        screen.blit(n.render(), n.get_pos())
        screen.blit(u.render(), u.get_pos())
        screen.blit(s.render(), s.get_pos())

