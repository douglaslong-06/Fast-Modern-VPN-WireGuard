"""SharedProcessor module."""

import math
import random


class SharedProcessor:
    """Small compute_manager helper."""

    def __init__(self, seed: int = 9) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_manager(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 9) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 9


def main() -> None:
    obj = SharedProcessor()
    print(obj.compute_manager(9))


if __name__ == "__main__":
    main()
