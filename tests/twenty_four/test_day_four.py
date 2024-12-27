import pytest
from expects import equal, expect

from src.twenty_four.day_four import DayFour


class TestDayFour:
    @staticmethod
    def example() -> list[str]:
        return open("inputs/twenty_four/04.example").read().strip().split("\n")

    @staticmethod
    def real_input() -> list[str]:
        return open("inputs/twenty_four/04.in").read().strip().split("\n")

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 18),
            (real_input(), 2536),
        ],
    )
    def test_part_one(self, input: list[str], solution: int) -> None:
        day = DayFour(input)

        result = day.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 9),
            (real_input(), 1875),
        ],
    )
    def test_part_two(self, input: list[str], solution: int) -> None:
        day = DayFour(input)

        result = day.part_two()

        expect(result).to(equal(solution))
