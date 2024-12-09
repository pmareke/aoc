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
        for position, size, file_id in reversed(files):
            for space_i, (space_pos, space_size) in enumerate(spaces):
                if space_pos < position and size <= space_size:
                    for idx in range(size):
                        checksum[position + idx] = None
                        checksum[space_pos + idx] = file_id
                    spaces[space_i] = (space_pos + size, space_size - size)
                    break

        result = 0
        for idx, digit in enumerate(checksum):
            if digit:
                result += idx * digit
        return result
