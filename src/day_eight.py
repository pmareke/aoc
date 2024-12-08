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
                    if idx < 0 or idy < 0:
                        continue
                    if idx >= len(antennas) or idy >= len(antennas[idx]):
                        continue
                    if antennas[point_x][point_y] == antennas[idx][idy]:
                        dx = (2 * point_x) - idx
                        dy = (2 * point_y) - idy
                        if dx > len(antennas) - 1 or dy > len(antennas[0]) - 1:
                            continue
                        if dx < 0 or dy < 0:
                            continue
                        antinodes.append((dx, dy))
        return antinodes

    def _find_extra_antinodes(self, antennas: list, point_x: int, point_y: int) -> list:
        antinodes = []
        movements = [-1, 0, 1]
        for movement in movements:
            for idx in range(len(antennas) - (point_x * movement)):
                for idy in range(len(antennas[0]) - (point_y * movement)):
                    if point_x == idx and point_y == idy:
                        continue
                    if idx < 0 or idy < 0:
                        continue
                    if idx >= len(antennas) or idy >= len(antennas[idx]):
                        continue
                    if antennas[point_x][point_y] == antennas[idx][idy]:
                        delta = 0
                        dx = idx - point_x
                        dy = idy - point_y
                        while True:
                            xx = point_x - (dx * delta)
                            yy = point_y - (dy * delta)
                            if xx > len(antennas) - 1 or yy > len(antennas[0]) - 1:
                                break
                            if xx < 0 or yy < 0:
                                break
                            antinodes.append((xx, yy))
                            delta += 1
        return antinodes
