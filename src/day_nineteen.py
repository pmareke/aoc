from functools import cache


class DayNineteen:
    def __init__(self, input: str) -> None:
        self.patterns, self.designs = self._parse_input(input)
        self.max_len = max(map(len, self.patterns))

    def part_one(self) -> int:
        return sum(1 for design in self.designs if self._is_valid(design))

    def part_two(self) -> int:
        return sum(self._possibilities(design) for design in self.designs)

    def _parse_input(self, input: str) -> tuple:
        _patterns, _designs = input.split("\n\n")
        _patterns_list = _patterns.split(", ")
        patterns = sorted(_patterns_list, key=lambda x: len(x), reverse=True)
        designs = _designs.split("\n")
        return patterns, designs

    @cache
    def _is_valid(self, design: str) -> bool:
        if design == "":
            return True

        for idx in range(min(len(design), self.max_len) + 1):
            if design[:idx] in self.patterns and self._is_valid(design[idx:]):
                return True

        return False

    @cache
    def _possibilities(self, design: str) -> int:
        if design == "":
            return 1

        count = 0
        for idx in range(min(len(design), self.max_len) + 1):
            if design[:idx] in self.patterns:
                count += self._possibilities(design[idx:])
        return count
