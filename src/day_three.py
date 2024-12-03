import re


class DayThree:
    REGEX = r"mul\((\d{1,3},\d{1,3})\)"

    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        result = 0
        numbers = re.findall(self.REGEX, self.input)
        for pair in numbers:
            x, y = list(map(int, pair.split(",")))
            result += x * y
        return result

    def part_two(self) -> int:
        first_block = True
        result = 0
        parts = self.input.split("don't()")
        for part in parts:
            if first_block:
                numbers = re.findall(self.REGEX, part)
                for pair in numbers:
                    x, y = list(map(int, pair.split(",")))
                    result += x * y
                first_block = False
                continue

            do_block_inside_dont = part.split("do()")
            for item in do_block_inside_dont[1:]:
                numbers = re.findall(self.REGEX, item)
                for pair in numbers:
                    x, y = list(map(int, pair.split(",")))
                    result += x * y

        return result
