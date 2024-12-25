import pytest
from expects import equal, expect

from src.twenty_four.day_fifteen import DayFifteen


class TestDayFifteen:
    @staticmethod
    def small_example() -> str:
        return open("inputs/2024/15.example").read().strip()

    @staticmethod
    def example() -> str:
        return open("inputs/2024/15.example2").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/2024/15.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (small_example(), 2028),
            (example(), 10092),
            (real_input(), 1360570),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayFifteen(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (small_example(), 1751),
            (example(), 9021),
            (real_input(), 1381446),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DayFifteen(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
