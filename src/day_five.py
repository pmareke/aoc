from collections import defaultdict


class DayFive:
    def __init__(self, input: str) -> None:
        self.rules, self.updates = self._parse_input(input)

    def part_one(self) -> int:
        valid_rules = []
        for update in self.updates:
            valid = self._is_valid(update)
            if valid:
                valid_rules.append(update)

        result = 0
        for rule in valid_rules:
            middle = (len(rule) - 1) / 2
            result += rule[int(middle)]
        return result

    def part_two(self) -> int:
        invalid_updates = []
        for update in self.updates:
            valid = self._is_valid(update)
            if not valid:
                invalid_updates.append(update)

            for update in invalid_updates:
                valid = False
                while not valid:
                    for n in update:
                        numbers_in_rule = [x for x in self.rules[n] if x in update]
                        for x in numbers_in_rule:
                            idx = update.index(n)
                            idy = update.index(x)
                            if idx > idy:
                                update[idx], update[idy] = update[idy], update[idx]
                    valid = self._is_valid(update)

        result = 0
        for update in invalid_updates:
            middle = (len(update) - 1) / 2
            result += update[int(middle)]
        return result

    def _parse_input(self, input: str) -> tuple[dict[int, list[int]], list[list[int]]]:
        rules = defaultdict(list)
        updates = []
        parts = input.split("\n\n")

        pairs = parts[0].split("\n")
        for pair in pairs:
            before, after = list(map(int, pair.strip().split("|")))
            rules[before].append(after)

        pairs = parts[1].split("\n")
        for pair in pairs:
            numbers = list(map(int, pair.strip().split(",")))
            updates.append(numbers)
        return rules, updates

    def _is_valid(self, update: list[int]) -> bool:
        seen = set()
        valid = True
        for number in update:
            next = self.rules[number]
            for n in next:
                if n in update and n in seen:
                    valid = False
            seen.add(number)
        return valid
