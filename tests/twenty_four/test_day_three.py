import pytest
from expects import equal, expect

from src.twenty_four.day_three import DayThree


class TestDayThree:
    @staticmethod
    def example() -> str:
        return open("inputs/twenty_four/03.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/twenty_four/03.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 161),
            (real_input(), 187194524),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day = DayThree(input)

        result = day.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 48),
            (real_input(), 127092535),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day = DayThree(input)

        result = day.part_two()

        expect(result).to(equal(solution))
