class DayTwenty:
    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self, input: str) -> None:
        self.start, self.maze = self._parse_input(input)
        self.rows, self.cols = len(self.maze), len(self.maze[0])

    def part_one(self, nanoseconds: int) -> int:
        dists = self._calculate_distances()
        count = 0
        for idx in range(self.rows):
            for idy in range(self.cols):
                if self.maze[idx][idy] == "#":
                    continue
                for dx, dy in [
                    (idx + 2, idy),
                    (idx + 1, idy + 1),
                    (idx, idy + 2),
                    (idx - 1, idy + 1),
                ]:
                    if dx < 0 or dy < 0 or dx >= self.rows or dy >= self.cols:
                        continue
                    if self.maze[dx][dy] == "#":
                        continue
                    if abs(dists[idx][idy] - dists[dx][dy]) >= nanoseconds + 2:
                        count += 1
        return count

    def part_two(self, nanoseconds: int) -> int:
        dists = self._calculate_distances()
        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze[r][c] == "#":
                    continue
                for radius in range(2, 21):
                    for dr in range(radius + 1):
                        dc = radius - dr
                        for nr, nc in {
                            (r + dr, c + dc),
                            (r + dr, c - dc),
                            (r - dr, c + dc),
                            (r - dr, c - dc),
                        }:
                            if nr < 0 or nc < 0 or nr >= self.rows or nc >= self.cols:
                                continue
                            if self.maze[nr][nc] == "#":
                                continue
                            if dists[r][c] - dists[nr][nc] >= nanoseconds + radius:
                                count += 1
        return count

    def _parse_input(self, input: str) -> tuple:
        start = (0, 0)
        maze = []
        for idx, line in enumerate(input.split("\n")):
            _line = []
            for idy, char in enumerate(line):
                if char == "S":
                    start = (idx, idy)
                _line.append(char)
            maze.append(_line)
        return start, maze

    def _calculate_distances(self) -> list:
        x, y = self.start
        dists = [[-1] * self.cols for _ in range(self.rows)]
        dists[x][y] = 0

        while self.maze[x][y] != "E":
            for dx, dy in self.DIRS:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= self.rows or ny >= self.cols:
                    continue
                if self.maze[nx][ny] == "#":
                    continue
                if dists[nx][ny] != -1:
                    continue
                dists[nx][ny] = dists[x][y] + 1
                x = nx
                y = ny

        return dists
