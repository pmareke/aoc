import pytest
from expects import equal, expect

from src.twenty_four.day_eight import DayEight


class TestDayEight:
    @staticmethod
    def example() -> str:
        return open("inputs/twenty_four/08.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/twenty_four/08.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 14),
            (real_input(), 381),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayEight(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 34),
            (real_input(), 1184),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DayEight(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
