import heapq
from collections import deque


class DaySixteen:
    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        map, start = self._parse_input()
        min_cost = self._walk(map, start)
        return min_cost

    def part_two(self) -> int:
        map, start = self._parse_input()
        seen = self._walk2(map, start)
        return len({(x, y) for x, y, _, _ in seen})

    def _parse_input(self) -> tuple[list, tuple]:
        start = (-1, -1)
        map = []
        for idx, column in enumerate(self.input.split("\n")):
            line = []
            for idy, row in enumerate(column):
                if row == "S":
                    start = (idx, idy)
                line.append(row)
            map.append(line)
        return map, start

    def _walk(self, map: list, start: tuple) -> int:
        priority_queue = [(0, start[0], start[1], 0, 1)]
        seen = {(start[0], start[1], 0, 1)}
        min_cost = 0
        while priority_queue:
            cost, x, y, dx, dy = heapq.heappop(priority_queue)
            seen.add((x, y, dx, dy))
            if map[x][y] == "E":
                min_cost = cost
                break
            for new_cost, xx, yy, dxx, dyy in [
                (cost + 1, x + dx, y + dy, dx, dy),
                (cost + 1000, x, y, dy, -dx),
                (cost + 1000, x, y, -dy, dx),
            ]:
                if map[xx][yy] == "#":
                    continue
                if (xx, yy, dxx, dyy) in seen:
                    continue
                heapq.heappush(priority_queue, (new_cost, xx, yy, dxx, dyy))
        return min_cost

    def _walk2(self, map: list, start: tuple) -> set:
        priority_queue = [(0, start[0], start[1], 0, 1)]
        lowest_cost = {(start[0], start[1], 0, 1): 0}
        backtrack: dict[tuple, set] = {}
        best_cost = float("inf")
        end_states = set()

        while priority_queue:
            cost, x, y, dx, dy = heapq.heappop(priority_queue)
            if cost > lowest_cost.get((x, y, dx, dy), float("inf")):
                continue
            if map[x][y] == "E":
                if cost > best_cost:
                    break
                best_cost = cost
                end_states.add((x, y, dx, dy))
            for new_cost, xx, yy, dxx, dyy in [
                (cost + 1, x + dx, y + dy, dx, dy),
                (cost + 1000, x, y, dy, -dx),
                (cost + 1000, x, y, -dy, dx),
            ]:
                if map[xx][yy] == "#":
                    continue
                lowest = lowest_cost.get((xx, yy, dxx, dyy), float("inf"))
                if new_cost > lowest:
                    continue
                if new_cost < lowest:
                    backtrack[(xx, yy, dxx, dyy)] = set()
                    lowest_cost[(xx, yy, dxx, dyy)] = new_cost
                backtrack[(xx, yy, dxx, dyy)].add((x, y, dx, dy))
                heapq.heappush(priority_queue, (new_cost, xx, yy, dxx, dyy))

        states = deque(end_states)
        seen = set(end_states)
        while states:
            key = states.popleft()
            for last in backtrack.get(key, []):
                if last in seen:
                    continue
                seen.add(last)
                states.append(last)

        return seen
