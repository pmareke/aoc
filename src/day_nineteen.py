class DayNineteen:
    def __init__(self, input: str) -> None:
        self.patterns, self.designs = self._parse_input(input)

    def part_one(self) -> int:
        total = 0
        for design in self.designs:
            ways = self._ways(design, {})
            if ways > 0:
                total += 1
        return total

    def part_two(self) -> int:
        return sum(self._ways(design, {}) for design in self.designs)

    def _parse_input(self, input: str) -> tuple:
        _patterns, _designs = input.split("\n\n")
        _patterns_list = _patterns.split(", ")
        patterns = sorted(_patterns_list, key=lambda x: len(x), reverse=True)
        designs = _designs.split("\n")
        return patterns, designs

    def _ways(self, target: str, seen: dict[str, int]) -> int:
        if target in seen:
            return seen[target]

        ways = 0

        if not target:
            ways = 1

        for pattern in self.patterns:
            if target.startswith(pattern):
                ways += self._ways(target[len(pattern) :], seen)

        seen[target] = ways
        return ways
