class DaySeven:
    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        result = 0
        for line in self.input.split("\n"):
            _target, _numbers = line.strip().split(": ")
            target = int(_target)
            numbers = list(map(int, _numbers.strip().split(" ")))
            if self._resolves_to_target(target, numbers):
                result += target
        return result

    def part_two(self) -> int:
        result = 0
        for line in self.input.split("\n"):
            _target, _numbers = line.strip().split(": ")
            target = int(_target)
            numbers = list(map(int, _numbers.strip().split(" ")))
            if self._resolves_to_target_v2(target, numbers):
                result += target
        return result

    def _resolves_to_target(self, target: int, numbers: list[int]) -> bool:
        if len(numbers) == 1:
            return numbers[0] == target

        x, y = numbers[:2]
        tail = numbers[2:]
        if self._resolves_to_target(target, [x * y] + tail):
            return True
        if self._resolves_to_target(target, [x + y] + tail):
            return True
        return False

    def _resolves_to_target_v2(self, target: int, numbers: list[int]) -> bool:
        if len(numbers) == 1:
            return numbers[0] == target

        x, y = numbers[:2]
        tail = numbers[2:]
        if self._resolves_to_target_v2(target, [x * y] + tail):
            return True
        if self._resolves_to_target_v2(target, [x + y] + tail):
            return True
        if self._resolves_to_target_v2(target, [int(f"{x}{y}")] + tail):
            return True
        return False
