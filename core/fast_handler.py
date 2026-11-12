"""SmartSession module."""

import math
import random


class SmartSession:
    """Small load_registry helper."""

    def __init__(self, seed: int = 10) -> None:
        self._state = seed
        self._items: list[int] = []

    def load_registry(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 10) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 10


def main() -> None:
    obj = SmartSession()
    print(obj.load_registry(10))


if __name__ == "__main__":
    main()
