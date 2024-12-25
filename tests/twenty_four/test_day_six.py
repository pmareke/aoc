import pytest
from expects import equal, expect

from src.twenty_four.day_six import DaySix


class TestDaySix:
    @staticmethod
    def example() -> str:
        return open("inputs/twenty_four/06.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/twenty_four/06.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 41),
            (real_input(), 4890),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day_one = DaySix(input)

        result = day_one.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 6),
            (real_input(), 1995),
        ],
    )
    def test_part_two(self, input: str, solution: int) -> None:
        day_one = DaySix(input)

        result = day_one.part_two()

        expect(result).to(equal(solution))
