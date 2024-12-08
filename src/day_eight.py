class DayEight:
    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        antennas = self._get_antennas()
        antinodes = set()
        for idx, column in enumerate(antennas):
            for idy, row in enumerate(column):
                if row == ".":
                    continue
                _antinodes = self._find_antinodes(antennas, idx, idy)
                antinodes.update(_antinodes)
        return len(antinodes)

    def part_two(self) -> int:
        antennas = self._get_antennas()
        antinodes = set()
        for idx, column in enumerate(antennas):
            for idy, row in enumerate(column):
                if row == ".":
                    continue
                _antinodes = self._find_extra_antinodes(antennas, idx, idy)
                antinodes.update(_antinodes)
        return len(antinodes)

    def _get_antennas(self) -> list:
        antennas = []
        for line in self.input.split("\n"):
            antennas.append(list(line))
        return antennas

    def _find_antinodes(self, antennas: list, point_x: int, point_y: int) -> list:
        antinodes = []
        movements = [-1, 0, 1]
        for movement in movements:
            for idx in range(len(antennas) - (point_x * movement)):
                for idy in range(len(antennas[0]) - (point_y * movement)):
                    if point_x == idx and point_y == idy:
                        continue
                    if idx >= len(antennas) or idy >= len(antennas[idx]):
                        continue

                    if antennas[point_x][point_y] == antennas[idx][idy]:
                        x = (2 * point_x) - idx
                        y = (2 * point_y) - idy
                        if self._is_out_of_bounds(antennas, x, y):
                            continue
                        antinode = (x, y)
                        antinodes.append(antinode)
        return antinodes

    def _find_extra_antinodes(self, antennas: list, point_x: int, point_y: int) -> list:
        antinodes = []
        movements = [-1, 0, 1]
        for movement in movements:
            for idx in range(len(antennas) - (point_x * movement)):
                for idy in range(len(antennas[0]) - (point_y * movement)):
                    if point_x == idx and point_y == idy:
                        continue
                    if idx >= len(antennas) or idy >= len(antennas[idx]):
                        continue
                    if antennas[point_x][point_y] == antennas[idx][idy]:
                        delta = 0
                        dx = idx - point_x
                        dy = idy - point_y
                        while True:
                            x = point_x - (dx * delta)
                            y = point_y - (dy * delta)
                            if self._is_out_of_bounds(antennas, x, y):
                                break
                            antinode = (x, y)
                            antinodes.append(antinode)
                            delta += 1
        return antinodes

    @staticmethod
    def _is_out_of_bounds(anntenas: list, x: int, y: int) -> bool:
        if x < 0 or y < 0:
            return True
        return x >= len(anntenas) or y >= len(anntenas[x])
