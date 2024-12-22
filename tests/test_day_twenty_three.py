import pytest
from expects import equal, expect

from src.day_twenty_three import DayTwentyThree


class TestDayTwentyThree:
    @staticmethod
    def example() -> str:
        return open("inputs/23.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/23.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 0),
            (real_input(), 0),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayTwentyThree(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 0),
            (real_input(), 0),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DayTwentyThree(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
