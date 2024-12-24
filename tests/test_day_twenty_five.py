import pytest
from expects import equal, expect

from src.day_twenty_five import DayTwentyFive


class TestDayTwentyFive:
    @staticmethod
    def example() -> str:
        return open("inputs/08.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/08.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 0),
            (real_input(), 0),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayTwentyFive(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))
