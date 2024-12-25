from collections import defaultdict


class DayOne:
    def __init__(self, input: list[str]) -> None:
        self.input = input

    def part_one(self) -> int:
        left = []
        right = []
        for line in self.input:
            _left, _right = list(map(int, line.split("   ")))
            left.append(_left)
            right.append(_right)
        return self._total_distance(left, right)

    def _total_distance(self, left: list[int], right: list[int]) -> int:
        left = sorted(left)
        right = sorted(right)
        result = 0
        for _left, _right in zip(left, right):
            result += abs(_left - _right)
        return result

    def part_two(self) -> int:
        left = []
        right: dict[int, int] = defaultdict(int)
        for line in self.input:
            _left, _right = list(map(int, line.split("   ")))
            left.append(_left)
            right[_right] += 1

        return self._calculate_similarity(left, right)

    def _calculate_similarity(self, left: list[int], right: dict[int, int]) -> int:
        result = 0
        for idx, item in enumerate(left):
            result += item * right[item]
        return result
