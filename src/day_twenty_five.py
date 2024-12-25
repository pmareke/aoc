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
                    lock_weight = lock[idx]
                    key_weight = len(key) - key[idx] + 1
                    if lock_weight >= key_weight:
                        overlapping = True
                if not overlapping:
                    total += 1
        return total

    def _parse_input(self) -> tuple[list[list[int]], list[list[int]]]:
        locks = []
        keys = []
        for blocks in self.input.split("\n\n"):
            block = blocks.split("\n")
            is_block = False
            if block[0] == "#" * len(block[0]):
                is_block = True
            weights = [0] * len(block[0])
            for idx in range(1, len(block) - 1):
                for idy, char in enumerate(block[idx]):
                    if is_block:
                        weights[idy] = idx if char == "#" else weights[idy]
                    if weights[idy] == 0:
                        position = len(block) - idx - 1
                        weights[idy] = position if char == "#" else weights[idy]
            if is_block:
                locks.append(weights)
                continue
            keys.append(weights)
        return locks, keys
