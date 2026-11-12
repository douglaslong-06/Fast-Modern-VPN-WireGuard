"""CoreClient module."""

import math
import random


class CoreClient:
    """Small dispatch_cache helper."""

    def __init__(self, seed: int = 96) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_cache(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 96) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 96


def main() -> None:
    obj = CoreClient()
    print(obj.dispatch_cache(96))


if __name__ == "__main__":
    main()
