"""DynamicClient module."""

import math
import random


class DynamicClient:
    """Small handle_monitor helper."""

    def __init__(self, seed: int = 58) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_monitor(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 58) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 58


def main() -> None:
    obj = DynamicClient()
    print(obj.handle_monitor(58))


if __name__ == "__main__":
    main()
