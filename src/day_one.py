from collections import defaultdict


class DayOne:
    def __init__(self, input: list[str]) -> None:
        self.input = input

    def part_one(self) -> int:
        left = []
        right = []
        for line in self.input:
            numbers = line.split("   ")
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))
        return self._total_distance(left, right)

    def _total_distance(self, left: list[int], right: list[int]) -> int:
        left = sorted(left)
        right = sorted(right)

        result = 0
        for idx, item in enumerate(left):
            result += abs(item - right[idx])
        return result

    def part_two(self) -> int:
        left = []
        right: dict[int, int] = defaultdict(int)
        for line in self.input:
            numbers = line.split("   ")
            left.append(int(numbers[0]))
            right[int(numbers[1])] += 1

        return self._calculate_similarity(left, right)

    def _calculate_similarity(self, left: list[int], right: dict[int, int]) -> int:
        result = 0
        for idx, item in enumerate(left):
            result += item * right[item]
        return result
