import pytest
from expects import equal, expect

from src.twenty_four.day_eleven import DayEleven


class TestDayEleven:
    @staticmethod
    def example() -> str:
        return open("inputs/twenty_four/11.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/twenty_four/11.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 55312),
            (real_input(), 231278),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day = DayEleven(input)

        result = day.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 65601038650482),
            (real_input(), 274229228071551),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day = DayEleven(input)

        result = day.part_two()

        expect(result).to(equal(solution))
