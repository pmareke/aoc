import pytest
from expects import equal, expect

from src.day_two import DayTwo


class TestDayTwo:
    @pytest.fixture
    def input(self) -> list[str]:
        return open("inputs/02.in").read().strip().split("\n")

    def test_part_one(self, input: list[str]) -> None:
        day_one = DayTwo(input)

        result = day_one.part_one()

        expect(result).to(equal(549))

    def test_part_two(self, input: list[str]) -> None:
        day_one = DayTwo(input)

        result = day_one.part_two()

        expect(result).to(equal(589))
