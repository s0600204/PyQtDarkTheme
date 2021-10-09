from __future__ import annotations

import math
from functools import lru_cache


class RGBA:
    def __init__(self, r: float, g: float, b: float, a: float = 1) -> None:
        self._r = min(255, max(0, r))
        self._g = min(255, max(0, g))
        self._b = min(255, max(0, b))
        self._a = max(min(1, a), 0)

    def __str__(self) -> str:
        return f"rgba({self.r:.3f}, {self.g:.3f}, {self.b:.3f}, {self.a:.3f})"

    def __getitem__(self, item: int) -> float:
        return [self.r, self.g, self.b, self.a][item]

    @property
    def r(self) -> float:
        return self._r

    @property
    def g(self) -> float:
        return self._g

    @property
    def b(self) -> float:
        return self._b

    @property
    def a(self) -> float:
        return self._a

    @staticmethod
    @lru_cache()
    def from_hex(hex: str) -> RGBA:
        hex = hex.lstrip("#")
        r, g, b, a = 255, 0, 0, 1
        if len(hex) == 3:  # #RGB format
            r, g, b = [int(char, 16) for char in hex]
            r, g, b = 16 * r + r, 16 * g + g, 16 * b + b
        if len(hex) == 4:  # #RGBA format
            r, g, b, a = [int(char, 16) for char in hex]
            r, g, b = 16 * r + r, 16 * g + g, 16 * b + b
            a = (16 * a + a) / 255
        if len(hex) == 6:  # #RRGGBB format
            r, g, b = bytes.fromhex(hex)
            a = 1
        elif len(hex) == 8:  # #RRGGBBAA format
            r, g, b, a = bytes.fromhex(hex)
            a = a / 255
        return RGBA(r, g, b, a)

    @staticmethod
    @lru_cache()
    def to_hex(rgba: RGBA) -> str:
        r, g, b, a = rgba
        return f"{math.floor(r):x}{math.floor(g):x}{math.floor(b):x}{math.floor(a*255):02x}"