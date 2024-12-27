import pytest
from expects import equal, expect

from src.twenty_three.day_three import DayThree


class TestDayThree:
    @staticmethod
    def example() -> list[str]:
        return open("inputs/twenty_three/03.example").read().strip().split("\n")

    @staticmethod
    def real_input() -> list[str]:
        return open("inputs/twenty_three/03.in").read().strip().split("\n")

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 0),
            (real_input(), 0),
        ],
    )
    def test_part_one(self, input: list[str], solution: int) -> None:
        day = DayThree(input)

        result = day.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 0),
            (real_input(), 0),
        ],
    )
    def test_part_two(self, input: list[str], solution: int) -> None:
        day = DayThree(input)

        result = day.part_two()

        expect(result).to(equal(solution))
