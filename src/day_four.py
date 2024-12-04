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
                        if [dx + (dX * 2), dy + (dY * 2)] in A:
                            if [dx + (dX * 3), dy + (dY * 3)] in S:
                                result += 1
        return result

    def part_two(self) -> int:
        result = 0

        M = self._search_letter_positions("M")
        A = self._search_letter_positions("A")
        S = self._search_letter_positions("S")

        for a in A:
            x, y = a
            up_left = [x - 1, y - 1]
            down_left = [x + 1, y - 1]
            up_right = [x - 1, y + 1]
            down_right = [x + 1, y + 1]
            if up_left in M and down_left in M and up_right in S and down_right in S:
                result += 1
            if up_left in S and down_left in S and up_right in M and down_right in M:
                result += 1
            if up_left in S and down_left in M and up_right in S and down_right in M:
                result += 1
            if up_left in M and down_left in S and up_right in M and down_right in S:
                result += 1
        return result

    def _search_letter_positions(self, letter: str) -> list[list[int]]:
        positions = []
        for idx, line in enumerate(self.puzzle):
            for idy, char in enumerate(line):
                if char == letter:
                    positions.append([idx, idy])
        return positions
