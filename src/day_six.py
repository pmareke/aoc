class DaySix:
    def __init__(self, input: str) -> None:
        self.maze = input.split("\n")

    def part_one(self) -> int:
        rows = len(self.maze)
        columns = len(self.maze[0])
        direction = 0
        point_x, point_y = self._find_starting_point()
        seen = set()
        while True:
            seen.add((point_x, point_y))

            dx, dy = self.direction_points(direction)
            new_point_x, new_point_y = [point_x + dx, point_y + dy]

            if not (0 <= new_point_x < rows and 0 <= new_point_y < columns):
                break

            if self.maze[new_point_x][new_point_y] == "#":
                direction = (direction + 1) % 4
                continue

            point_x, point_y = new_point_x, new_point_y
        return len(seen)

    def part_two(self) -> int:
        rows = len(self.maze)
        columns = len(self.maze[0])
        loops = 0
        for idx in range(rows):
            for idy in range(columns):
                point_x, point_y = self._find_starting_point()
                direction = 0
                SEEN = set()
                while True:
                    if (direction, point_x, point_y) in SEEN:
                        loops += 1
                        break

                    SEEN.add((direction, point_x, point_y))

                    dx, dy = self.direction_points(direction)
                    new_point_x, new_point_y = [point_x + dx, point_y + dy]

                    if not (0 <= new_point_x < rows and 0 <= new_point_y < columns):
                        break

                    if self.maze[new_point_x][new_point_y] == "#":
                        direction = (direction + 1) % 4
                        continue

                    if [new_point_x, new_point_y] == [idx, idy]:
                        direction = (direction + 1) % 4
                        continue

                    point_x, point_y = new_point_x, new_point_y
        return loops

    def _find_starting_point(self) -> list[int]:
        for idx, line in enumerate(self.maze):
            for idy, position in enumerate(line):
                if position == "^":
                    return [idx, idy]
        raise Exception("No starting point found")

    def direction_points(self, direction: int) -> tuple[int, int]:
        return [(-1, 0), (0, 1), (1, 0), (0, -1)][direction]
