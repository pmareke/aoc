import pytest
from expects import equal, expect

from src.day_thirteen import DayThirteen


class TestDayThirteen:
    @staticmethod
    def example() -> str:
        return open("inputs/13.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/13.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 480),
            (real_input(), 29388),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayThirteen(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 875318608908),
            (real_input(), 99548032866004),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DayThirteen(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
