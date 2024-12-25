class DayTwentyFour:
    def __init__(self, input: str) -> None:
        parts = input.split("\n\n")
        self.known = {}
        for line in parts[0].split("\n"):
            if line.isspace():
                break
            x, y = line.split(": ")
            self.known[x] = int(y)

        self.formulas = {}
        for line in parts[1].split("\n"):
            x, op, y, z = line.replace(" -> ", " ").split()
            self.formulas[z] = (op, x, y)
        self.operators = {
            "OR": lambda x, y: x | y,
            "AND": lambda x, y: x & y,
            "XOR": lambda x, y: x ^ y,
        }

    def part_one(self) -> int:
        z = []
        i = 0

        while True:
            key = "z" + str(i).rjust(2, "0")
            if key not in self.formulas:
                break
            z.append(self._calc(key))
            i += 1

        return int("".join(map(str, z[::-1])), 2)

    def part_two(self) -> str:
        swaps = []
        for _ in range(4):
            baseline = self._progress()
            for x in self.formulas:
                for y in self.formulas:
                    if x == y:
                        continue
                    self.formulas[x], self.formulas[y] = (
                        self.formulas[y],
                        self.formulas[x],
                    )
                    if self._progress() > baseline:
                        break
                    self.formulas[x], self.formulas[y] = (
                        self.formulas[y],
                        self.formulas[x],
                    )
                else:
                    continue
                break
            swaps += [x, y]

        return ",".join(sorted(swaps))

    def _calc(self, wire: str) -> int:
        if wire in self.known:
            return self.known[wire]
        op, x, y = self.formulas[wire]
        self.known[wire] = self.operators[op](self._calc(x), self._calc(y))
        return self.known[wire]

    def _make_wire(self, char: str, num: int) -> str:
        return char + str(num).rjust(2, "0")

    def _verify_z(self, wire: str, num: int) -> bool:
        if wire not in self.formulas:
            return False
        op, x, y = self.formulas[wire]
        if op != "XOR":
            return False
        if num == 0:
            return sorted([x, y]) == ["x00", "y00"]
        return (
            self._verify_intermediate_xor(x, num)
            and self._verify_carry_bit(y, num)
            or self._verify_intermediate_xor(y, num)
            and self._verify_carry_bit(x, num)
        )

    def _verify_intermediate_xor(self, wire: str, num: int) -> bool:
        if wire not in self.formulas:
            return False
        op, x, y = self.formulas[wire]
        if op != "XOR":
            return False
        return sorted([x, y]) == [self._make_wire("x", num), self._make_wire("y", num)]

    def _verify_carry_bit(self, wire: str, num: int) -> bool:
        if wire not in self.formulas:
            return False
        op, x, y = self.formulas[wire]
        if num == 1:
            if op != "AND":
                return False
            return sorted([x, y]) == ["x00", "y00"]
        if op != "OR":
            return False
        return (
            self._verify_direct_carry(x, num - 1)
            and self._verify_recarry(y, num - 1)
            or self._verify_direct_carry(y, num - 1)
            and self._verify_recarry(x, num - 1)
        )

    def _verify_direct_carry(self, wire: str, num: int) -> bool:
        if wire not in self.formulas:
            return False
        op, x, y = self.formulas[wire]
        if op != "AND":
            return False
        return sorted([x, y]) == [self._make_wire("x", num), self._make_wire("y", num)]

    def _verify_recarry(self, wire: str, num: int) -> bool:
        if wire not in self.formulas:
            return False
        op, x, y = self.formulas[wire]
        if op != "AND":
            return False
        return (
            self._verify_intermediate_xor(x, num)
            and self._verify_carry_bit(y, num)
            or self._verify_intermediate_xor(y, num)
            and self._verify_carry_bit(x, num)
        )

    def _verify(self, num: int) -> bool:
        return self._verify_z(self._make_wire("z", num), num)

    def _progress(self) -> int:
        i = 0

        while True:
            if not self._verify(i):
                break
            i += 1

        return i
