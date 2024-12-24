from collections import defaultdict
from typing import Callable


class DayTwentyFour:
    def __init__(self, input: str) -> None:
        self.initial_values, self.cables = self.parse_input(input)

    def part_one(self) -> int:
        operations: list[str] = []
        while len(operations) < len(self.cables):
            for key, operation in self.cables.items():
                if key in operations:
                    continue
                x, y, op = operation
                if x in self.initial_values.keys() and y in self.initial_values.keys():
                    op1 = self.initial_values[x]
                    op2 = self.initial_values[y]
                    self.initial_values[key] = op(op1, op2)
                    operations.append(key)
        output = ""
        for key, value in sorted(self.initial_values.items(), reverse=True):
            if key.startswith("z"):
                output += str(value)
        return int(output, 2)

    def part_two(self) -> int:
        return 0

    def parse_input(
        self, input: str
    ) -> tuple[dict[str, int], dict[str, tuple[str, str, Callable]]]:
        initial_values = defaultdict(int)
        cables: dict[str, tuple[str, str, Callable]] = {}
        parts = input.strip().split("\n\n")
        for value in parts[0].split("\n"):
            key, value = value.split(": ")
            initial_values[key] = int(value)
        for cable in parts[1].split("\n"):
            operation, var = cable.split(" -> ")
            cables[var] = self.parse_operation(operation)
        return initial_values, cables

    def parse_operation(self, raw_operation: str) -> tuple[str, str, Callable]:
        x, operation, y = raw_operation.split(" ")
        return {
            "AND": (x, y, lambda x, y: x & y),
            "OR": (x, y, lambda x, y: x | y),
            "XOR": (x, y, lambda x, y: x ^ y),
        }[operation]
