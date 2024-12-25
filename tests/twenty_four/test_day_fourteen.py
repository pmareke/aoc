import pytest
from expects import equal, expect

from src.twenty_four.day_fourteen import DayFourteen


class TestDayFourteen:
    @staticmethod
    def real_input() -> str:
        return open("inputs/2024/14.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (real_input(), 215987200),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayFourteen(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (real_input(), 8050),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DayFourteen(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
