import re
from dataclasses import dataclass

from sympy import Eq, solve, symbols
from sympy.core.numbers import Integer


@dataclass
class Point:
    X: int
    Y: int


@dataclass
class Game:
    A: Point
    B: Point
    prize: Point


class DayThirteen:
    def __init__(self, input: str) -> None:
        self.games = self._parse_input(input)

    def part_one(self) -> int:
        total = 0
        for game in self.games:
            button_a = game.A
            button_b = game.B
            prize = game.prize
            total += self._solve(button_a, button_b, prize, factor=0)
        return total

    def part_two(self) -> int:
        total = 0
        for game in self.games:
            button_a = game.A
            button_b = game.B
            prize = game.prize
            total += self._solve(button_a, button_b, prize, factor=10000000000000)
        return total

    def _parse_input(self, input: str) -> list[Game]:
        games: list[Game] = []
        blocks = input.split("\n\n")
        for block in blocks:
            parts = block.split("\n")
            games.append(self._create_game(parts))
        return games

    def _create_game(self, parts: list) -> Game:
        regex = r"\d+"
        x, y = map(int, re.findall(regex, parts[0]))
        button_a = Point(x, y)
        x, y = map(int, re.findall(regex, parts[1]))
        button_b = Point(x, y)
        x, y = map(int, re.findall(regex, parts[2]))
        prize = Point(x, y)
        return Game(button_a, button_b, prize)

    def _solve(self, A: Point, B: Point, prize: Point, factor: int) -> int:
        x, y = symbols("x y")
        x_prize = prize.X + factor
        eq1 = Eq(A.X * x + B.X * y, x_prize)
        y_prize = prize.Y + factor
        eq2 = Eq(A.Y * x + B.Y * y, y_prize)

        solution = solve((eq1, eq2), (x, y))
        if isinstance(solution[x], Integer) and isinstance(solution[y], Integer):
            x = solution[x]
            y = solution[y]
            return int(x * 3 + y)
        return 0
