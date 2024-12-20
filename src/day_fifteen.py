class DayFifteen:
    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        no_expansion = {"#": "#", "O": "O", ".": ".", "@": "@"}
        map, starting_point, movements = self._parse_input(self.input, no_expansion)
        self._move_boxes(map, starting_point, movements)
        return self._calculate_score(map, "O")

    def part_two(self) -> int:
        expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}
        map, starting_point, movements = self._parse_input(self.input, expansion)
        self._move_wider_boxes(map, starting_point, movements)
        return self._calculate_score(map, "[")

    def _parse_input(self, input: str, expansion: dict) -> tuple:
        map, movements = input.strip().split("\n\n")
        maze = []
        for column in map.split("\n"):
            line = []
            for row in column:
                line.extend(list("".join(expansion[row])))
            maze.append(line)
        starting_point = None
        for idx, _column in enumerate(maze):
            for idy, _row in enumerate(_column):
                if _row == "@":
                    starting_point = (idx, idy)
        return maze, starting_point, "".join(movements.split("\n"))

    def _move_boxes(self, map: list, starting_point: tuple, movements: str) -> None:
        x, y = starting_point
        for move in movements:
            dx = {"^": -1, "v": 1}.get(move, 0)
            dy = {"<": -1, ">": 1}.get(move, 0)
            targets = [(x, y)]
            current_x = x
            current_y = y
            valid = True
            while True:
                current_x += dx
                current_y += dy
                point = map[current_x][current_y]
                if point == "#":
                    valid = False
                    break
                if point == "O":
                    targets.append((current_x, current_y))
                if point == ".":
                    break
            if not valid:
                continue
            map[x][y] = "."
            map[x + dx][y + dy] = "@"
            for target in targets[1:]:
                map[target[0] + dx][target[1] + dy] = "O"
            x += dx
            y += dy

    def _move_wider_boxes(
        self, map: list, starting_point: tuple, movements: str
    ) -> None:
        x, y = starting_point
        for move in movements:
            dx = {"^": -1, "v": 1}.get(move, 0)
            dy = {"<": -1, ">": 1}.get(move, 0)
            targets = [(x, y)]
            valid = True
            for cr, cc in targets:
                next_x = cr + dx
                next_y = cc + dy
                if (next_x, next_y) in targets:
                    continue
                point = map[next_x][next_y]
                if point == "#":
                    valid = False
                if point == "[":
                    targets.append((next_x, next_y))
                    targets.append((next_x, next_y + 1))
                if point == "]":
                    targets.append((next_x, next_y))
                    targets.append((next_x, next_y - 1))
            if not valid:
                continue
            map_copy = [list(row) for row in map]
            map[x][y] = "."
            map[x + dx][y + dy] = "@"
            for previous_x, previous_y in targets[1:]:
                map[previous_x][previous_y] = "."
            for previous_x, previous_y in targets[1:]:
                map[previous_x + dx][previous_y + dy] = map_copy[previous_x][previous_y]
            x += dx
            y += dy

    def _calculate_score(self, map: list[list[str]], selector: str) -> int:
        boxes = []
        for idx, column in enumerate(map):
            for idy, row in enumerate(column):
                if row == selector:
                    boxes.append((idx, idy))
        return sum(100 * x + y for x, y in boxes)
