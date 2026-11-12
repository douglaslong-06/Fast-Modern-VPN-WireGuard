"""LiteSession module."""

import math
import random


class LiteSession:
    """Small parse_controller helper."""

    def __init__(self, seed: int = 71) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_controller(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 71) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 71


def main() -> None:
    obj = LiteSession()
    print(obj.parse_controller(71))


if __name__ == "__main__":
    main()
