class DaySix:
    def __init__(self, input: str) -> None:
        self.starting_point, self._point, self.maze = self._parse_input(input)

    def part_one(self) -> int:
        point = self._point
        direction = [-1, 0]
        next_position = self.starting_point
        seen = set()
        while True:
            xx, yy = next_position
            seen.add((xx, yy))

            xx, yy = [next_position[0] + direction[0], next_position[1] + direction[1]]

            if not (0 <= xx < len(self.maze) and 0 <= yy < len(self.maze[0])):
                break

            if self.maze[xx][yy] == "#":
                point, direction = self._change_direction(point, direction)
                continue

            next_position = [xx, yy]
            seen.add((xx, yy))

        return len(seen)

    def part_two(self) -> int:
        loops = 0
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                point = self._point
                x, y = self.starting_point
                direction = [-1, 0]
                SEEN = set()
                while True:
                    if ((point, x, y)) in SEEN:
                        loops += 1
                        break

                    SEEN.add((point, x, y))

                    xx, yy = [x + direction[0], y + direction[1]]

                    if not (0 <= xx < len(self.maze) and 0 <= yy < len(self.maze[0])):
                        break

                    if self.maze[xx][yy] == "#" or [xx, yy] == [i, j]:
                        point, direction = self._change_direction(point, direction)
                        continue

                    x, y = xx, yy
        return loops

    def _parse_input(
        self, input: str
    ) -> tuple[list[int, int], list[int, int], list[list[str]]]:
        point = ""
        starting_point = [0, 0]
        maze = []
        for idx, line in enumerate(input.split("\n")):
            for idy, position in enumerate(line):
                if position not in [".", "#"]:
                    point = position
                    starting_point = [idx, idy]
            maze.append(list(line))
        return starting_point, point, maze

    def _change_direction(
        self, point: tuple[int, int], direction: tuple[int, int]
    ) -> tuple[str, tuple[int, int]]:
        return {
            ">": ("v", [1, 0]),
            "<": ("^", [-1, 0]),
            "^": (">", [0, 1]),
            "v": ("<", [0, -1]),
        }[point]
