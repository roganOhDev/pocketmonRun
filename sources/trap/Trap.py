from pygame import Surface

from sources.common.Object import Object


class Trap(Object):
    image: Surface

# TODO 떨어지는것도 빈칸으로 따로 넣어야함(jump 의 조건때문에)
