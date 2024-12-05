from collections import defaultdict


class DayFive:
    def __init__(self, input: str) -> None:
        self.rules, self.updates = self._parse_input(input)

    def part_one(self) -> int:
        valid_updates = [update for update in self.updates if self._is_valid(update)]
        return self._calculate(valid_updates)

    def part_two(self) -> int:
        invalid_updates = [
            update for update in self.updates if not self._is_valid(update)
        ]
        for update in invalid_updates:
            while not self._is_valid(update):
                update = self._fix_update(update)
        return self._calculate(invalid_updates)

    def _parse_input(self, input: str) -> tuple[dict[int, list[int]], list[list[int]]]:
        parts = input.split("\n\n")
        _rules = parts[0].split("\n")
        _updates = parts[1].split("\n")

        rules = defaultdict(list)
        for pair in _rules:
            before, after = list(map(int, pair.strip().split("|")))
            rules[before].append(after)

        updates = []
        for pair in _updates:
            numbers = list(map(int, pair.strip().split(",")))
            updates.append(numbers)
        return rules, updates

    def _is_valid(self, update: list[int]) -> bool:
        seen = set()
        valid = True
        for number in update:
            next = self.rules[number]
            for _number in next:
                if _number in update and _number in seen:
                    valid = False
            seen.add(number)
        return valid

    def _fix_update(self, update: list[int]) -> list[int]:
        for number in update:
            numbers_in_rule = [x for x in self.rules[number] if x in update]
            for x in numbers_in_rule:
                idx = update.index(number)
                idy = update.index(x)
                if idx > idy:
                    update[idx], update[idy] = update[idy], update[idx]
        return update

    def _calculate(self, updates: list[list[int]]) -> int:
        result = 0
        for update in updates:
            middle = (len(update) - 1) / 2
            result += update[int(middle)]
        return result
