from collections import deque
from functools import cache
from itertools import product


class DayTwentyOne:
    NUM_KEYPAD = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
    DIR_KEYPAD = [[None, "^", "A"], ["<", "v", ">"]]

    def __init__(self, input: str) -> None:
        self.input = input
        self.num_seqs = self._compute_seqs(self.NUM_KEYPAD)
        self.dir_seqs = self._compute_seqs(self.DIR_KEYPAD)
        self.dir_lengths = {key: len(value[0]) for key, value in self.dir_seqs.items()}

    def part_one(self) -> int:
        total = 0
        for line in self.input.splitlines():
            robot1 = self._solve(line, self.num_seqs)
            next = robot1
            for _ in range(2):
                possible_next = []
                for seq in next:
                    possible_next += self._solve(seq, self.dir_seqs)
                minlen = min(map(len, possible_next))
                next = [seq for seq in possible_next if len(seq) == minlen]
            total += len(next[0]) * int(line[:-1])
        return total

    def part_two(self) -> int:
        total = 0
        for line in self.input.splitlines():
            inputs = self._solve(line, self.num_seqs)
            length = min(map(self._compute_length, inputs))
            total += length * int(line[:-1])
        return total

    def _compute_seqs(self, keypad: list) -> dict[tuple, list[str]]:
        position = {}
        for row in range(len(keypad)):
            for column in range(len(keypad[row])):
                if keypad[row][column] is not None:
                    position[keypad[row][column]] = (row, column)
        seqs = {}
        for idx in position:
            for idy in position:
                if idx == idy:
                    seqs[(idx, idy)] = ["A"]
                    continue
                possibilities = []
                queue = deque([(position[idx], "")])
                optimal = float("inf")
                while queue:
                    (row, column), moves = queue.popleft()
                    for nr, nc, nm in [
                        (row - 1, column, "^"),
                        (row + 1, column, "v"),
                        (row, column - 1, "<"),
                        (row, column + 1, ">"),
                    ]:
                        if (
                            nr < 0
                            or nc < 0
                            or nr >= len(keypad)
                            or nc >= len(keypad[0])
                        ):
                            continue
                        if keypad[nr][nc] is None:
                            continue
                        if keypad[nr][nc] == idy:
                            if optimal < len(moves) + 1:
                                break
                            optimal = len(moves) + 1
                            possibilities.append(moves + nm + "A")
                        else:
                            queue.append(((nr, nc), moves + nm))
                    else:
                        continue
                    break
                seqs[(idx, idy)] = possibilities
        return seqs

    def _solve(self, string: str, seqs: dict) -> list[str]:
        options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
        return ["".join(x) for x in product(*options)]

    @cache
    def _compute_length(self, seq: str, depth: int = 25) -> int:
        if depth == 1:
            return sum(self.dir_lengths[(x, y)] for x, y in zip("A" + seq, seq))
        length = 0
        for x, y in zip("A" + seq, seq):
            tmp = []
            for subseq in self.dir_seqs[(x, y)]:
                tmp.append(self._compute_length(subseq, depth - 1))
            length += min(tmp)
        return length
