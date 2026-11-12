"""DynamicCollector module."""

import math
import random


class DynamicCollector:
    """Small load_session helper."""

    def __init__(self, seed: int = 62) -> None:
        self._state = seed
        self._items: list[int] = []

    def load_session(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 62) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 62


def main() -> None:
    obj = DynamicCollector()
    print(obj.load_session(62))


if __name__ == "__main__":
    main()
