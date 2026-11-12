"""StreamManager module."""

import math
import random


class StreamManager:
    """Small fetch_loader helper."""

    def __init__(self, seed: int = 87) -> None:
        self._state = seed
        self._items: list[int] = []

    def fetch_loader(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 87) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 87


def main() -> None:
    obj = StreamManager()
    print(obj.fetch_loader(87))


if __name__ == "__main__":
    main()
