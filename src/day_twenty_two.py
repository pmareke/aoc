from collections import defaultdict


class DayTwentyTwo:
    def __init__(self, input: str) -> None:
        self.numbers = list(map(int, input.split("\n")))

    def part_one(self) -> int:
        total = 0
        for number in self.numbers:
            next = number
            for idx in range(2000):
                next = self._calculate_secret(next)
            total += next
        return total

    def part_two(self) -> int:
        total: dict[tuple, int] = defaultdict(int)
        for number in self.numbers:
            next = number
            buyer = [number % 10]
            for idx in range(2000):
                next = self._calculate_secret(next)
                buyer.append(next % 10)
            seen = set()
            for idx in range(len(buyer) - 4):
                a, b, c, d, e = buyer[idx : idx + 5]
                diffs = (b - a, c - b, d - c, e - d)
                if diffs in seen:
                    continue
                seen.add(diffs)
                total[diffs] += e

        return max(total.values())

    def _calculate_secret(self, number: int) -> int:
        x = (number ^ number * 64) % 16777216
        x = (x ^ x // 32) % 16777216
        x = (x ^ x * 2048) % 16777216
        return x
