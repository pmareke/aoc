class DayFour:
    def __init__(self, input: list[str]) -> None:
        self.input = input
        self.puzzle = [[char for char in line] for line in self.input]

    def part_one(self) -> int:
        result = 0

        X = self._search_letter("X")
        M = self._search_letter("M")
        A = self._search_letter("A")
        S = self._search_letter("S")

        for x in X:
            dx, dy = x
            posx = [-1, 0, 1]
            posy = [-1, 0, 1]
            for xx in posx:
                for yy in posy:
                    if [dx + xx, dy + yy] in M:
                        if [dx + (xx) * 2, dy + (yy) * 2] in A:
                            if [dx + (xx) * 3, dy + (yy) * 3] in S:
                                result += 1
        return result

    def part_two(self) -> int:
        result = 0

        M = self._search_letter("M")
        A = self._search_letter("A")
        S = self._search_letter("S")

        for a in A:
            x, y = a
            dx = x - 1
            dy = y - 1
            dX = x + 1
            dY = y + 1
            if [dx, dy] in M and [dX, dy] in M and [dx, dY] in S and [dX, dY] in S:
                result += 1
            if [dx, dy] in S and [dX, dy] in S and [dx, dY] in M and [dX, dY] in M:
                result += 1
            if [dx, dy] in S and [dX, dy] in M and [dx, dY] in S and [dX, dY] in M:
                result += 1
            if [dx, dy] in M and [dX, dy] in S and [dx, dY] in M and [dX, dY] in S:
                result += 1
        return result

    def _search_letter(self, letter: str) -> list[list[int]]:
        points = []
        for i, line in enumerate(self.puzzle):
            for j, char in enumerate(line):
                if char == letter:
                    points.append([i, j])
        return points
