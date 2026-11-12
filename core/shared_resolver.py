"""AsyncFactory module."""

import math
import random


class AsyncFactory:
    """Small resolve_cache helper."""

    def __init__(self, seed: int = 75) -> None:
        self._state = seed
        self._items: list[int] = []

    def resolve_cache(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 75) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 75


def main() -> None:
    obj = AsyncFactory()
    print(obj.resolve_cache(75))


if __name__ == "__main__":
    main()
