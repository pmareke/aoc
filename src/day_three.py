import re


class DayThree:
    REGEX = r"mul\((\d{1,3},\d{1,3})\)"

    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        return self._calculate(self.input)

    def part_two(self) -> int:
        result = 0
        [before_first_dont, *rest] = self.input.split("don't()")
        result += self._calculate(before_first_dont)
        for part in rest:
            [_, *do_block_inside_dont] = part.split("do()")
            for block in do_block_inside_dont:
                result += self._calculate(block)
        return result

    def _calculate(self, input: str) -> int:
        result = 0
        numbers = re.findall(self.REGEX, input)
        for pair in numbers:
            x, y = list(map(int, pair.split(",")))
            result += x * y
        return result
