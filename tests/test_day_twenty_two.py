import pytest
from expects import equal, expect

from src.day_twenty_two import DayTwentyTwo


class TestDayTwentyTwo:
    @staticmethod
    def example() -> str:
        return open("inputs/22.example").read().strip()

    @staticmethod
    def another_example() -> str:
        return open("inputs/22.example2").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/22.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 37327623),
            (real_input(), 13022553808),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DayTwentyTwo(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (another_example(), 23),
            (real_input(), 1555),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DayTwentyTwo(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))