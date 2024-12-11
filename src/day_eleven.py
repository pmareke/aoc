from functools import cache


class DayEleven:
    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        stones = list(map(int, self.input.split(" ")))
        total = 0
        for stone in stones:
            total += self._calculate_stones(stone, 25)
        return total

    def part_two(self) -> int:
        stones = list(map(int, self.input.split(" ")))
        total = 0
        for stone in stones:
            total += self._calculate_stones(stone, 75)
        return total

    @cache
    def _calculate_stones(self, stone: int, times: int) -> int:
        if times == 0:
            return 1

        if stone == 0:
            result = self._calculate_stones(1, times - 1)
            return result

        if len(str(stone)) % 2 == 0:
            middle = len(str(stone)) // 2
            left = int(str(stone)[:middle])
            right = int(str(stone)[middle:])
            left_result = self._calculate_stones(int(left), times - 1)
            right_result = self._calculate_stones(int(right), times - 1)
            result = left_result + right_result
            return result

        result = self._calculate_stones(stone * 2024, times - 1)
        return result
