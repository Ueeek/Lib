from typing import *
from __future__ import annotations


class P:
    def __init__(self, x:int, y:int, N:int):
        self.pos = (x, y)
        self.N = N

    def __str__(self) -> str:
        x, y = self.pos
        return "(x:{} y:{})".format(x, y)

    def __eq__(self, other:P) -> bool:
        if other is None:
            return False

        x, y = self.pos
        xx, yy = other.pos
        return x == xx and y == yy

    def toInt(self) -> int:
        x, y = self.pos
        return x*self.N+y

    def fromInt(self, val:int) -> Optional[P]:
        return P(val//self.N, val % self.N, self.N)

    def copy(self) -> Optional[P]:
        x, y = self.pos
        return P(x, y, self.N)

    def dist_1(self, other:P)->int:
        return abs(self.pos[0]- other.pos[0]) + abs(self.pos[1]- other.pos[1])
        


class P_Factory:
    def __init__(self, N):
        self.N = N

    def create(self, x, y) -> P:
        return P(x, y, self.N)

    def yield_all_pos(self) -> Iterable[P]:
        for x in range(self.N):
            for y in range(self.N):
                yield P(x, y, self.N)
