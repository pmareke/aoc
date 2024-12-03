import pytest
from expects import equal, expect

from src.day_three import DayThree


class TestDayThree:
    @staticmethod
    def example() -> str:
        return open("inputs/03.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/03.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 161),
            (real_input(), 187194524),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayThree(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 48),
            (real_input(), 127092535),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DayThree(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
