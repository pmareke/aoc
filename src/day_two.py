class DayTwo:
    def __init__(self, input: list[str]) -> None:
        self.input = input

    def part_one(self) -> int:
        result = 0
        for line in self.input:
            numbers = list(map(int, line.split()))
            if self._is_safe(numbers):
                result += 1
        return result

    def part_two(self) -> int:
        result = 0
        for line in self.input:
            numbers = list(map(int, line.split()))
            if self._is_safe_v2(numbers):
                result += 1
        return result

    def _is_safe(self, numbers: list[int]) -> bool:
        desc = sorted(numbers, reverse=True)
        if numbers == desc:
            if self._is_valid(desc):
                return True

        asc = sorted(numbers)
        if numbers == asc:
            if self._is_valid(asc):
                return True

        return False

    def _is_safe_v2(self, numbers: list[int]) -> bool:
        for i in range(len(numbers)):
            valid_numbers = [*numbers[:i], *numbers[i + 1 :]]
            if self._is_safe(valid_numbers):
                return True
        return False

    def _is_valid(self, numbers: list[int]) -> bool:
        for i in range(len(numbers) - 1):
            diff = abs(numbers[i] - numbers[i + 1])
            if diff < 1 or diff > 3:
                return False
        return True
