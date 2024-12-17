import pytest
from expects import equal, expect

from src.day_seventeen import DaySeventeen


class TestDaySeventeen:
    @staticmethod
    def example() -> str:
        return open("inputs/17.example").read().strip()

    @staticmethod
    def another_example() -> str:
        return open("inputs/17.example2").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/17.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), "4,6,3,5,6,3,5,2,1,0"),
            (real_input(), "6,2,7,2,3,1,6,0,5"),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DaySeventeen(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (another_example(), 14680),
            (real_input(), 236548287712877),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DaySeventeen(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
