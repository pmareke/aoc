import pytest
from expects import equal, expect

from src.twenty_three.day_two import DayTwo


class TestDayTwo:
    @staticmethod
    def example() -> list[str]:
        return open("inputs/twenty_three/02.example").read().strip().split("\n")

    @staticmethod
    def real_input() -> list[str]:
        return open("inputs/twenty_three/02.in").read().strip().split("\n")

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 8),
            (real_input(), 2101),
        ],
    )
    def test_part_one(self, input: list[str], solution: int) -> None:
        day = DayTwo(input)

        result = day.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 2286),
            (real_input(), 58269),
        ],
    )
    def test_part_two(self, input: list[str], solution: int) -> None:
        day = DayTwo(input)

        result = day.part_two()

        expect(result).to(equal(solution))
