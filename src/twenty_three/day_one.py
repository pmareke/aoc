import re


class DayOne:
    def __init__(self, input: list[str]) -> None:
        self.lines = input

    def part_one(self) -> int:
        regex = r"(\d)"
        total = 0
        for line in self.lines:
            numbers = re.findall(regex, line)
            if len(numbers) == 1:
                total += int(numbers[0] * 2)
                continue
            total += int(f"{numbers[0]}{numbers[-1]}")
        return total

    def part_two(self) -> int:
        regex = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
        total = 0
        for line in self.lines:
            numbers = re.findall(regex, line)
            if len(numbers) == 1:
                total += int(self._raw_to_num(numbers[0]) * 2)
                continue
            number = f"{self._raw_to_num(numbers[0])}{self._raw_to_num(numbers[-1])}"
            total += int(number)
        return total

    def _raw_to_num(self, num: str) -> str:
        return {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }.get(num, num)
