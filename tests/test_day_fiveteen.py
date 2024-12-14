import pytest
from expects import equal, expect

from src.day_fiveteen import DayFiveteen


class TestDayFiveteen:
    @staticmethod
    def example() -> str:
        return open("inputs/15.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/15.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 0),
            (real_input(), 0),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayFiveteen(input)

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
        day_one = DayFiveteen(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
