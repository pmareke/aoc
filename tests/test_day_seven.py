import pytest
from expects import equal, expect

from src.day_seven import DaySeven


class TestDaySeven:
    @staticmethod
    def example() -> str:
        return open("inputs/07.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/07.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 3749),
            (real_input(), 20665830408335),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DaySeven(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 11387),
            (real_input(), 354060705047464),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DaySeven(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
