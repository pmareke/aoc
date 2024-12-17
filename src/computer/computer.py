from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Computer:
    A: int
    B: int
    C: int
    instructions: list[int]
    pointer: int = 0
    output: list[int] = field(default_factory=list)
    output2: int | None = None

    def run(self) -> str:
        while True:
            try:
                operation = self._instructions(self.instructions[self.pointer])
                combo = self.instructions[self.pointer + 1]
                operation(combo)
            except IndexError:
                break
        return ",".join(map(str, self.output))

    def find(self, target: list, register: int) -> int | None:
        if target == []:
            return register

        for b in range(8):
            self.A = register << 3 | b
            self.B = 0
            self.C = 0
            self.output2 = None
            for pointer in range(0, len(self.instructions) - 2, 2):
                ins = self.instructions[pointer]
                operand = self.instructions[pointer + 1]
                if ins == 1:
                    self.B ^= operand
                if ins == 2:
                    self.B = self._combo(operand) % 8
                if ins == 4:
                    self.B ^= self.C
                if ins == 5:
                    self.output2 = self._combo(operand) % 8
                if ins == 6:
                    self.B = self.A >> self._combo(operand)
                if ins == 7:
                    self.C = self.A >> self._combo(operand)

                if self.output2 == target[-1]:
                    sub = self.find(target[:-1], self.A)
                    if sub is None:
                        continue
                    return sub

        return None

    def _instructions(self, opcode: int) -> Callable:
        return {
            0: self._adv,
            1: self._bxl,
            2: self._bst,
            3: self._jnz,
            4: self._bxc,
            5: self._out,
            6: self._bdv,
            7: self._cdv,
        }[opcode]

    def _adv(self, operand: int) -> None:
        self.A = self.A // (2 ** self._combo(operand))
        self.pointer += 2

    def _bxl(self, operand: int) -> None:
        self.B ^= operand
        self.pointer += 2

    def _bst(self, operand: int) -> None:
        self.B = self._combo(operand) % 8
        self.pointer += 2

    def _jnz(self, operand: int) -> None:
        next_pointer = operand if self.A != 0 else self.pointer + 2
        self.pointer = next_pointer

    def _bxc(self, _operand: int) -> None:
        self.B ^= self.C
        self.pointer += 2

    def _out(self, operand: int) -> None:
        modulo = self._combo(operand) % 8
        self.output.append(modulo)
        self.pointer += 2

    def _bdv(self, operand: int) -> None:
        self.B = self.A // (2 ** self._combo(operand))
        self.pointer += 2

    def _cdv(self, operand: int) -> None:
        self.C = self.A // (2 ** self._combo(operand))
        self.pointer += 2

    def _combo(self, operand: int) -> int:
        if operand == 7:
            raise Exception("Invalid operand")

        return {4: self.A, 5: self.B, 6: self.C}.get(operand, operand)
