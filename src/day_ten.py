import re
from collections import defaultdict


class DayTen:
    def __init__(self, input: str) -> None:
        self.input = input
        self.map = self._parse_input()

    def part_one(self) -> int:
        trailheads = self._calculate_trailheads()
        result = 0
        for start, hills in trailheads.items():
            result += len(set(hills))
        return result

    def part_two(self) -> int:
        trailheads = self._calculate_trailheads()
        result = 0
        for start, hills in trailheads.items():
            result += len(hills)
        return result

    def _parse_input(self) -> list:
        return [list(map(int, list(row))) for row in self.input.split("\n")]

    def _calculate_trailheads(self) -> dict:
        trailheads: dict[tuple, list[tuple]] = defaultdict(list)
        columns = len(self.map)
        rows = len(self.map[0])
        for column in range(columns):
            for row in range(rows):
                if self.map[column][row] == 0:
                    start = (column, row)
                    self._path(start, column, row, trailheads)
        return trailheads

    def _path(self, start: tuple, column: int, row: int, trailsheads: dict) -> None:
        if self.map[column][row] == 9:
            trailsheads[start].append((column, row))

        current = self.map[column][row]
        if row > 0 and current + 1 == self.map[column][row - 1]:
            self._path(start, column, row - 1, trailsheads)

        if row < len(self.map[0]) - 1 and current + 1 == self.map[column][row + 1]:
            self._path(start, column, row + 1, trailsheads)

        if column > 0 and current + 1 == self.map[column - 1][row]:
            self._path(start, column - 1, row, trailsheads)

        if column < len(self.map) - 1 and current + 1 == self.map[column + 1][row]:
            self._path(start, column + 1, row, trailsheads)
