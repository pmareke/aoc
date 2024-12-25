import pytest
from expects import equal, expect

from src.twenty_four.day_five import DayFive


class TestDayFive:
    @staticmethod
    def example() -> str:
        return open("inputs/twenty_four/05.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/twenty_four/05.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 143),
            (real_input(), 4957),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayFive(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 123),
            (real_input(), 6938),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DayFive(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
