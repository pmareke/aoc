import pytest
from expects import equal, expect

from src.twenty_four.day_twenty import DayTwenty


class TestDayTwenty:
    @staticmethod
    def example() -> str:
        return open("inputs/twenty_four/20.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/twenty_four/20.in").read().strip()

    @pytest.mark.parametrize(
        "input, nanoseconds, solution",
        [
            (example(), 64, 1),
            (real_input(), 100, 1450),
        ],
    )
    def test_part_one(self, input: str, nanoseconds: int, solution: int) -> None:
        day = DayTwenty(input)

        result = day.part_one(nanoseconds)

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, nanoseconds, solution",
        [
            (example(), 64, 86),
            (real_input(), 100, 1015247),
        ],
    )
    def test_part_two(self, input: str, nanoseconds: int, solution: int) -> None:
        day = DayTwenty(input)

        result = day.part_two(nanoseconds)

        expect(result).to(equal(solution))
