import pytest
from expects import equal, expect

from src.twenty_four.day_twenty_four import DayTwentyFour


class TestDayTwentyFour:
    @staticmethod
    def example() -> str:
        return open("inputs/2024/24.example").read().strip()

    @staticmethod
    def another_example() -> str:
        return open("inputs/2024/24.example2").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/2024/24.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 4),
            (another_example(), 2024),
            (real_input(), 51745744348272),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayTwentyFour(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (real_input(), "bfq,bng,fjp,hkh,hmt,z18,z27,z31"),
        ],
    )
    def test_part_two(self, input: str, solution: str) -> None:
        day_one = DayTwentyFour(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
