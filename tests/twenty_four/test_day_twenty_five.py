import pytest
from expects import equal, expect

from src.twenty_four.day_twenty_five import DayTwentyFive


class TestDayTwentyFive:
    @staticmethod
    def example() -> str:
        return open("inputs/2024/25.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/2024/25.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 3),
            (real_input(), 3344),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayTwentyFive(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))
