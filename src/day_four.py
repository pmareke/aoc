class DayFour:
    def __init__(self, input: list[str]) -> None:
        self.input = input
        self.puzzle = [[char for char in line] for line in self.input]

    def part_one(self) -> int:
        result = 0

        X = self._search_letter_positions("X")
        M = self._search_letter_positions("M")
        A = self._search_letter_positions("A")
        S = self._search_letter_positions("S")

        for x in X:
            dx, dy = x
            posX = [-1, 0, 1]
            posX = [-1, 0, 1]
            for dX in posX:
                for dY in posX:
                    if [dx + dX, dy + dY] in M:
                        if [dx + (dX) * 2, dy + (dY) * 2] in A:
                            if [dx + (dX) * 3, dy + (dY) * 3] in S:
                                result += 1
        return result

    def part_two(self) -> int:
        result = 0

        M = self._search_letter_positions("M")
        A = self._search_letter_positions("A")
        S = self._search_letter_positions("S")

        for a in A:
            x, y = a
            dx = x - 1
            dX = x + 1
            dy = y - 1
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

    def _search_letter_positions(self, letter: str) -> list[list[int]]:
        positions = []
        for idx, line in enumerate(self.puzzle):
            for idy, char in enumerate(line):
                if char == letter:
                    positions.append([idx, idy])
        return positions
