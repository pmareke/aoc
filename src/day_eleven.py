from functools import cache


class DayEleven:
    def __init__(self, input: str) -> None:
        self.stones = list(map(int, input.split()))

    def part_one(self) -> int:
        return sum(self._count(stone, 25) for stone in self.stones)

    def part_two(self) -> int:
        return sum(self._count(stone, 75) for stone in self.stones)

    @cache
    def _count(self, stone: int, steps: int) -> int:
        if steps == 0:
            return 1

        if stone == 0:
            return self._count(1, steps - 1)

        length = len(str(stone))
        if length % 2 == 0:
            middle = length // 2
            left = int(str(stone)[:middle])
            right = int(str(stone)[middle:])
            left_result = self._count(int(left), steps - 1)
            right_result = self._count(int(right), steps - 1)
            return left_result + right_result

        return self._count(stone * 2024, steps - 1)
