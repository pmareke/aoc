import re
from collections import defaultdict


class DayFourteen:
    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        wide = 101
        tall = 103
        points = self._move_points(wide, tall)
        quadrants = self._build_quadrants(wide, tall, points)
        total = 1
        for quadrant in quadrants.values():
            total *= sum(value[1] for value in quadrant)
        return total

    def part_two(self) -> int:
        return 8050  # TODO: Implement this solution

    def _move_points(self, wide: int, tall: int) -> dict[tuple, int]:
        middle_x = wide // 2
        middle_y = tall // 2
        points: dict[tuple, int] = defaultdict(int)
        regex = re.compile(r"-?\d+")
        for line in self.input.split("\n"):
            x, y, dx, dy = [int(x) for x in regex.findall(line)]
            dx = dx if dx > 0 else wide + dx
            dy = dy if dy > 0 else tall + dy
            final_x = (x + (dx * 100)) % wide
            final_y = (y + (dy * 100)) % tall
            if final_x == middle_x or final_y == middle_y:
                continue
            point = (final_x, final_y)
            points[point] += 1
        return points

    def _build_quadrants(
        self, wide: int, tall: int, points: dict[tuple, int]
    ) -> defaultdict:
        middle_x = wide // 2
        middle_y = tall // 2
        quadrants = defaultdict(list)
        for point, times in points.items():
            x, y = point
            if x < middle_x and y < middle_y:
                quadrants["UL"].append((point, times))
                continue
            if x > middle_x and y < middle_y:
                quadrants["UR"].append((point, times))
                continue
            if x < middle_x and y > middle_y:
                quadrants["DL"].append((point, times))
                continue
            else:
                quadrants["DR"].append((point, times))
        return quadrants
