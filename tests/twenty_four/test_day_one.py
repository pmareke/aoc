import pytest
from expects import equal, expect

from src.twenty_four.day_one import DayOne


class TestDayOne:
    @staticmethod
    def example() -> list[str]:
        return open("inputs/2024/01.example").read().strip().split("\n")

    @staticmethod
    def real_input() -> list[str]:
        return open("inputs/2024/01.in").read().strip().split("\n")

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 11),
            (real_input(), 3574690),
        ],
    )
    def test_part_one(self, input: list[str], solution: int) -> None:
        day_one = DayOne(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 31),
            (real_input(), 22565391),
        ],
    )
    def test_part_two(self, input: list[str], solution: int) -> None:
        day_one = DayOne(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
