import pytest
from expects import equal, expect

from src.day_eighteen import DayEighteen


class TestDayEightenn:
    @staticmethod
    def example() -> str:
        return open("inputs/18.example").read().strip()

    @staticmethod
    def real_input() -> str:
        return open("inputs/18.in").read().strip()

    @pytest.mark.parametrize(
        "input, rows, cols, times, solution",
        [
            (example(), 7, 7, 12, 22),
            (real_input(), 71, 71, 1024, 288),
        ],
    )
    def test_part_one(
        self,
        input: str,
        rows: int,
        cols: int,
        times: int,
        solution: int,
    ) -> None:
        day_one = DayEighteen(input)

        result = day_one.part_one(rows, cols, times)

        expect(result).to(equal(solution))

    @pytest.mark.parametrize(
        "input, rows, cols, solution",
        [
            (example(), 7, 7, "6,1"),
            (real_input(), 71, 71, "52,5"),
        ],
    )
    def test_part_two(
        self,
        input: str,
        rows: int,
        cols: int,
        solution: str,
    ) -> None:
        day_one = DayEighteen(input)

        result = day_one.part_two(rows, cols)

        expect(result).to(equal(solution))
