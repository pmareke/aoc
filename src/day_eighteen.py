import re
from collections import deque


class DayEighteen:
    def __init__(self, input: str) -> None:
        self.bytes = self._parse_bytes(input)

    def part_one(self, size: int, times: int) -> int:
        map = [["." for _ in range(size)] for _ in range(size)]
        for i in range(times):
            x, y = self.bytes[i]
            map[y][x] = "#"
        paths = self._walk(map, size)
        if not paths:
            return 0
        min_steps: int = min(paths)
        return min_steps

    def part_two(self, size: int) -> str:
        low = 0
        high = len(self.bytes)
        while low < high:
            middle = (low + high) // 2
            if self.part_one(size, middle + 1):
                low = middle + 1
            else:
                high = middle
        x, y = self.bytes[low]
        return f"{x},{y}"

    def _parse_bytes(self, input: str) -> list:
        regex = r"\d+"
        bytes = []
        for line in input.split("\n"):
            bytes.append(list(map(int, re.findall(regex, line))))
        return bytes

    def _walk(self, maze: list, size: int) -> list:
        paths = []
        queue: deque = deque([(0, 0, 0)])
        seen = set()
        while queue:
            y, x, steps = queue.popleft()
            if (y, x) in seen:
                continue
            seen.add((y, x))
            if (y, x) == (size - 1, size - 1):
                paths.append(steps)
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < size and 0 <= nx < size and maze[ny][nx] != "#":
                    queue.append((ny, nx, steps + 1))
        return paths
