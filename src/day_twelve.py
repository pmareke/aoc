from collections import deque


class DayTwelve:
    def __init__(self, input: str) -> None:
        self.map = [list(row) for row in input.split("\n")]

    def part_one(self) -> int:
        regions = self._generate_regions()
        return sum(len(region) * self._perimeter(region) for region in regions)

    def part_two(self) -> int:
        regions = self._generate_regions()
        return sum(len(region) * self._sides(region) for region in regions)

    def _generate_regions(self) -> list:
        rows = len(self.map)
        cols = len(self.map[0])
        regions = []
        seen = set()
        for row in range(rows):
            for column in range(cols):
                if (row, column) in seen:
                    continue
                seen.add((row, column))
                region = set()
                region.add((row, column))
                queue = deque([(row, column)])
                plant = self.map[row][column]
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if dx < 0 or dy < 0 or dx >= rows or dy >= cols:
                            continue
                        if self.map[dx][dy] != plant:
                            continue
                        if (dx, dy) in region:
                            continue
                        region.add((dx, dy))
                        queue.append((dx, dy))
                seen |= region
                regions.append(region)
        return regions

    def _perimeter(self, region: set) -> int:
        output = 0
        for x, y in region:
            output += 4
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                if (dx, dy) in region:
                    output -= 1
        return output

    def _sides(self, region: set) -> int:
        corner_candidates = set()
        for x, y in region:
            for dx, dy in [
                (x - 0.5, y - 0.5),
                (x + 0.5, y - 0.5),
                (x + 0.5, y + 0.5),
                (x - 0.5, y + 0.5),
            ]:
                corner_candidates.add((dx, dy))
        corners = 0
        for dx, dy in corner_candidates:
            config = [
                (sr, sc) in region
                for sr, sc in [
                    (dx - 0.5, dy - 0.5),
                    (dx + 0.5, dy - 0.5),
                    (dx + 0.5, dy + 0.5),
                    (dx - 0.5, dy + 0.5),
                ]
            ]
            number = sum(config)
            if number == 1:
                corners += 1
                continue

            if number == 2:
                if config == [True, False, True, False]:
                    corners += 2
                    continue
                if config == [False, True, False, True]:
                    corners += 2
                    continue

            if number == 3:
                corners += 1
        return corners
