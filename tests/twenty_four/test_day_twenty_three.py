import pytest
from expects import equal, expect

from src.twenty_four.day_twenty_three import DayTwentyThree


class TestDayTwentyThree:
    @staticmethod
    def example() -> str:
        return open("inputs/twenty_four/23.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/twenty_four/23.in").read().strip()

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), 7),
            (real_input(), 1304),
        ],
    )
    def test_part_one(self, input: str, solution: int) -> None:
        day = DayTwentyThree(input)

        result = day.part_one()

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, solution",
        [
            (example(), "co,de,ka,ta"),
            (real_input(), "ao,es,fe,if,in,io,ky,qq,rd,rn,rv,vc,vl"),
        ],
    )
    def test_part_two(self, input: str, solution: str) -> None:
        day = DayTwentyThree(input)

        result = day.part_two()

        expect(result).to(equal(solution))
