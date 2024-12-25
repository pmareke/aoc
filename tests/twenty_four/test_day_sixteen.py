import pytest
from expects import equal, expect

from src.twenty_four.day_sixteen import DaySixteen


class TestDaySixteen:
    @staticmethod
    def example() -> str:
        return open("inputs/twenty_four/16.example").read().strip()

    @staticmethod
    def another_example() -> str:
        return open("inputs/twenty_four/16.example2").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/twenty_four/16.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 7036),
            (another_example(), 11048),
            (real_input(), 65436),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DaySixteen(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 45),
            (another_example(), 64),
            (real_input(), 489),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DaySixteen(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
