import pytest
from expects import equal, expect

from src.twenty_four.day_twenty_one import DayTwentyOne


class TestDayTwentyOne:
    @staticmethod
    def example() -> str:
        return open("inputs/twenty_four/21.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/twenty_four/21.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 126384),
            (real_input(), 136780),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day = DayTwentyOne(input)

        result = day.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 154115708116294),
            (real_input(), 167538833832712),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day = DayTwentyOne(input)

        result = day.part_two()

        expect(result).to(equal(solution))
