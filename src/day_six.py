class DaySix:
    def __init__(self, input: str) -> None:
        self.input = input
        self.maze = input.split("\n")

    def part_one(self) -> int:
        direction = 0
        next_position = self._find_start()
        seen = set()
        while True:
            xx, yy = next_position
            seen.add((xx, yy))

            x, y = self._change_direction(direction)
            xx, yy = [next_position[0] + x, next_position[1] + y]

            if not (0 <= xx < len(self.maze) and 0 <= yy < len(self.maze[0])):
                break

            if self.maze[xx][yy] == "#":
                direction = (direction + 1) % 4
                continue

            next_position = [xx, yy]

        return len(seen)

    def part_two(self) -> int:
        loops = 0
        for idx in range(len(self.maze)):
            for idy in range(len(self.maze[0])):
                x, y = self._find_start()
                direction = 0
                SEEN = set()
                while True:
                    if ((direction, x, y)) in SEEN:
                        loops += 1
                        break

                    SEEN.add((direction, x, y))

                    dx, dy = self._change_direction(direction)
                    xx, yy = [x + dx, y + dy]

                    if not (0 <= xx < len(self.maze) and 0 <= yy < len(self.maze[0])):
                        break

                    if self.maze[xx][yy] == "#" or [xx, yy] == [idx, idy]:
                        direction = (direction + 1) % 4
                        continue

                    x, y = xx, yy
        return loops

    def _find_start(self) -> list[int]:
        for idx, line in enumerate(self.input.split("\n")):
            for idy, position in enumerate(line):
                if position not in [".", "#"]:
                    return [idx, idy]

    def _change_direction(self, direction: int) -> tuple[int, int]:
        return [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
        ][direction]
