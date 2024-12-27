import pytest
from expects import equal, expect

from src.twenty_four.day_eighteen import DayEighteen


class TestDayEightenn:
    @staticmethod
    def example() -> str:
        return open("inputs/twenty_four/18.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/twenty_four/18.in").read().strip()

    @pytest.mark.parametrize(
        "input, size, times, solution",
        [
            (example(), 7, 12, 22),
            (real_input(), 71, 1024, 288),
        ],
    )
    def test_part_one(
        self,
        input: str,
        size: int,
        times: int,
        solution: int,
    ) -> None:
        day = DayEighteen(input)

        result = day.part_one(size, times)

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, size, solution",
        [
            (example(), 7, "6,1"),
            (real_input(), 71, "52,5"),
        ],
    )
    def test_part_two(
        self,
        input: str,
        size: int,
        solution: str,
    ) -> None:
        day = DayEighteen(input)

        result = day.part_two(size)

        expect(result).to(equal(solution))
