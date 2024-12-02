class DayTwo:
    def __init__(self, input: list[str]) -> None:
        self.input = input

    def part_one(self) -> int:
        result = 0
        for line in self.input:
            numbers = list(map(int, line.split()))

            desc = sorted(numbers, reverse=True)
            if numbers == desc:
                if self._is_safe(desc):
                    result += 1
                continue

            asc = sorted(numbers)
            if numbers == asc:
                if self._is_safe(asc):
                    result += 1

        return result

    def part_two(self) -> int:
        result = 0
        for line in self.input:
            numbers = list(map(int, line.split()))

            desc = sorted(numbers, reverse=True)
            if numbers == desc:
                if self._is_safe(desc):
                    result += 1
                    continue

            asc = sorted(numbers)
            if numbers == asc:
                if self._is_safe(asc):
                    result += 1
                    continue

            valid_numbers = self.remove_one_level(numbers)
            if valid_numbers:
                result += 1

        return result

    def remove_one_level(self, numbers: list[int]) -> bool:
        for i in range(len(numbers)):
            valid_numbers = [*numbers[:i], *numbers[i + 1 :]]

            desc = sorted(valid_numbers, reverse=True)
            if valid_numbers == desc:
                if self._is_safe(desc):
                    return True

            asc = sorted(valid_numbers)
            if valid_numbers == asc:
                if self._is_safe(asc):
                    return True

        return False

    def _is_safe(self, numbers: list[int]) -> bool:
        for i in range(len(numbers) - 1):
            diff = abs(numbers[i] - numbers[i + 1])
            if diff < 1 or diff > 3:
                return False
        return True
