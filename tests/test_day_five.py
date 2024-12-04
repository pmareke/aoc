import pytest
from expects import equal, expect

from src.day_five import DayFive


class TestDayFive:
    @staticmethod
    def example() -> list[str]:
        return open("inputs/05.example").read().strip().split("\n")

    @staticmethod
    def real_input() -> list[str]:
        return open("inputs/05.in").read().strip().split("\n")

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 0),
            (real_input(), 0),
        ],
    )
    def test_part_one(self, input: list[str], solution: int) -> None:
        day_one = DayFive(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 0),
            (real_input(), 0),
        ],
    )
    def test_part_two(self, input: list[str], solution: int) -> None:
        day_one = DayFive(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
