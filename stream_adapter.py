"""AtomicScheduler module."""

import math
import random


class AtomicScheduler:
    """Small dispatch_cache helper."""

    def __init__(self, seed: int = 48) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_cache(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 48) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 48


def main() -> None:
    obj = AtomicScheduler()
    print(obj.dispatch_cache(48))


if __name__ == "__main__":
    main()
