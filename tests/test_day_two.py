import pytest
from expects import equal, expect

from src.day_two import DayTwo


class TestDayTwo:
    @staticmethod
    def example() -> list[str]:
        return open("inputs/02.example").read().strip().split("\n")

    @staticmethod
    def real_input() -> list[str]:
        return open("inputs/02.in").read().strip().split("\n")

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 2),
            (real_input(), 549),
        ],
    )
    def test_part_one(self, input: list[str], solution: int) -> None:
        day_one = DayTwo(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 4),
            (real_input(), 589),
        ],
    )
    def test_part_two(self, input: list[str], solution: int) -> None:
        day_one = DayTwo(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
