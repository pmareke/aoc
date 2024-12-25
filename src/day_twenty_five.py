class DayTwentyFive:
    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        locks, keys = self._parse_input()
        total = 0
        for lock in locks:
            for key in keys:
                overlapping = False
                for idx in range(len(lock)):
                    for idy in range(len(lock[idx])):
                        _lock = lock[idx][idy]
                        _key = key[idx][idy]
                        if _lock == "#" and _key == "#":
                            overlapping = True
                if not overlapping:
                    total += 1
        return total

    def _parse_input(self) -> tuple[list[list[str]], list[list[str]]]:
        locks = []
        keys = []
        for blocks in self.input.split("\n\n"):
            block = blocks.split("\n")
            chars = [row for row in block]
            if block[0][0] == "#":
                locks.append(chars)
                continue
            keys.append(chars)
        return locks, keys
