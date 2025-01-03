import pytest
from expects import equal, expect

from src.twenty_four.day_twelve import DayTwelve


class TestDayTwelve:
    @staticmethod
    def example() -> str:
        return open("inputs/twenty_four/12.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/twenty_four/12.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 1930),
            (real_input(), 1457298),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day = DayTwelve(input)

        result = day.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 1206),
            (real_input(), 921636),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day = DayTwelve(input)

        result = day.part_two()

        expect(result).to(equal(solution))
