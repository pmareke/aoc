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

    def _find_antinodes(self, antennas: list, x: int, y: int) -> list:
        antinodes = []
        d = [-1, 0, 1]
        for dd in d:
            for idx in range(len(antennas) - (x * dd)):
                for idy in range(len(antennas[0]) - (y * dd)):
                    if x == idx and y == idy:
                        continue
                    if idx < 0 or idy < 0:
                        continue
                    if idx >= len(antennas) or idy >= len(antennas[idx]):
                        continue
                    if antennas[x][y] == antennas[idx][idy]:
                        dx = idx - x
                        dy = idy - y
                        xx = x - dx
                        yy = y - dy
                        if xx > len(antennas) - 1 or yy > len(antennas[0]) - 1:
                            continue
                        if xx < 0 or yy < 0:
                            continue
                        antinodes.append((xx, yy))
        return antinodes

    def _find_extra_antinodes(self, antennas: list, x: int, y: int) -> list:
        antinodes = []
        d = [-1, 0, 1]
        for dd in d:
            for idx in range(len(antennas) - (x * dd)):
                for idy in range(len(antennas[0]) - (y * dd)):
                    if x == idx and y == idy:
                        continue
                    if idx < 0 or idy < 0:
                        continue
                    if idx >= len(antennas) or idy >= len(antennas[idx]):
                        continue
                    if antennas[x][y] == antennas[idx][idy]:
                        multipler = 0
                        dx = idx - x
                        dy = idy - y
                        while True:
                            xx = x - (dx * multipler)
                            yy = y - (dy * multipler)

                            if xx > len(antennas) - 1 or yy > len(antennas[0]) - 1:
                                break
                            if xx < 0 or yy < 0:
                                break
                            antinodes.append((xx, yy))
                            multipler += 1
        return antinodes
