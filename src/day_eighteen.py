import re
from collections import deque


class DayEighteen:
    def __init__(self, input: str) -> None:
        self.bytes = self._parse_bytes(input)

    def part_one(self, rows: int, cols: int, times: int) -> int:
        map = [["." for _ in range(rows)] for _ in range(cols)]
        maze = map.copy()
        for i in range(times):
            x, y = self.bytes[i]
            maze[y][x] = "#"
        paths = self._walk(maze, rows, cols)
        return min(len(path) for path in paths)

    def part_two(self, rows: int, cols: int) -> str:
        times = 1
        map = [["." for _ in range(rows)] for _ in range(cols)]
        while True:
            maze = map.copy()
            for t in range(times):
                x, y = self.bytes[t]
                maze[y][x] = "#"
            paths = self._walk(maze, rows, cols)
            if not paths:
                break
            times += 1
        return f"{self.bytes[times - 1][0]},{self.bytes[times - 1][1]}"

    def _parse_bytes(self, input: str) -> list:
        regex = r"\d+"
        bytes = []
        for line in input.split("\n"):
            bytes.append(list(map(int, re.findall(regex, line))))
        return bytes

    def _walk(self, maze: list, rows: int, cols: int) -> list:
        paths = []
        queue: deque = deque([(0, 0, [])])
        seen = set()
        while queue:
            y, x, current_path = queue.popleft()
            if (y, x) in seen:
                continue
            seen.add((y, x))
            if (y, x) == (cols - 1, rows - 1):
                paths.append(current_path)
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < cols and 0 <= nx < rows and maze[ny][nx] != "#":
                    queue.append((ny, nx, current_path + [(ny, nx)]))
        return paths
