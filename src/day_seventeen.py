from src.computer.computer import Computer


class DaySeventeen:
    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> str:
        computer = self._parse_input(self.input)
        return computer.run()

    def part_two(self) -> int:
        computer = self._parse_input(self.input)
        min = computer.find(computer.instructions, 0)
        assert min
        return min

    def _parse_input(self, input: str) -> Computer:
        registers, program = input.split("\n\n")
        A = int(registers.split("\n")[0].split("A: ")[1])
        B = int(registers.split("\n")[1].split("B: ")[1])
        C = int(registers.split("\n")[2].split("C: ")[1])
        instructions = list(map(int, program.split(": ")[1].split(",")))
        return Computer(A, B, C, instructions)
