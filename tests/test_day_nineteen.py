import pytest
from expects import equal, expect

from src.day_nineteen import DayNineteen


class TestDayNineteen:
    @staticmethod
    def example() -> str:
        return open("inputs/19.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/19.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 6),
            (real_input(), 342),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayNineteen(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 16),
            (real_input(), 891192814474630),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DayNineteen(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
