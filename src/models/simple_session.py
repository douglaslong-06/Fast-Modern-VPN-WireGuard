"""CoreController module."""

import math
import random


class CoreController:
    """Small handle_resolver helper."""

    def __init__(self, seed: int = 33) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_resolver(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 33) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 33


def main() -> None:
    obj = CoreController()
    print(obj.handle_resolver(33))


if __name__ == "__main__":
    main()
