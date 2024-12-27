import pytest
from expects import equal, expect

from src.twenty_three.day_one import DayOne


class TestDayOne:
    @staticmethod
    def example() -> list[str]:
        return open("inputs/twenty_three/01.example").read().strip().split("\n")

    @staticmethod
    def another_example() -> list[str]:
        return open("inputs/twenty_three/01.example2").read().strip().split("\n")

    @staticmethod
    def real_input() -> list[str]:
        return open("inputs/twenty_three/01.in").read().strip().split("\n")

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 142),
            (real_input(), 54632),
        ],
    )
    def test_part_one(self, input: list[str], solution: int) -> None:
        day = DayOne(input)

        result = day.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (another_example(), 281),
            (real_input(), 54019),
        ],
    )
    def test_part_two(self, input: list[str], solution: int) -> None:
        day = DayOne(input)

        result = day.part_two()

        expect(result).to(equal(solution))
