from collections import deque


class DayNine:
    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        FILES: deque[tuple] = deque([])
        SPACES: deque[tuple] = deque([])
        CHECKSUM: list[int | None] = []
        position = 0
        for idx, digit in enumerate(self.input):
            if idx % 2 == 0:
                index = idx // 2
                for idx in range(int(digit)):
                    CHECKSUM.append(index)
                    FILES.append((position, 1, index))
                    position += 1
                continue

            SPACES.append((position, int(digit)))
            for idx in range(int(digit)):
                CHECKSUM.append(None)
                position += 1

        return self._solve(FILES, SPACES, CHECKSUM)

    def part_two(self) -> int:
        FILES: deque[tuple] = deque([])
        SPACES: deque[tuple] = deque([])
        CHECKSUM: list[int | None] = []
        position = 0
        for idx, digit in enumerate(self.input):
            if idx % 2 == 0:
                index = idx // 2
                FILES.append((position, int(digit), index))
                for idx in range(int(digit)):
                    CHECKSUM.append(index)
                    position += 1
                continue

            SPACES.append((position, int(digit)))
            for idx in range(int(digit)):
                CHECKSUM.append(None)
                position += 1

        return self._solve(FILES, SPACES, CHECKSUM)

    def _solve(self, files: deque, spaces: deque, checksum: list[int | None]) -> int:
        for position, size, idx in reversed(files):
            for idy, (space_position, space_size) in enumerate(spaces):
                if space_position < position and size <= space_size:
                    for ids in range(size):
                        checksum[position + ids] = None
                        checksum[space_position + ids] = idx
                    spaces[idy] = (space_position + size, space_size - size)
                    break

        result = 0
        for ids, digit in enumerate(checksum):
            if digit is not None:
                result += ids * digit
        return result
