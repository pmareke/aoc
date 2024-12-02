import pytest
from expects import equal, expect

from src.day_three import DayThree


class TestDayThree:
    @pytest.fixture
    def input(self) -> list[str]:
        return open("inputs/03.in").read().strip().split("\n")

    def test_part_one(self, input: list[str]) -> None:
        day_one = DayThree(input)

        result = day_one.part_one()

        expect(result).to(equal(0))

    def test_part_two(self, input: list[str]) -> None:
        day_one = DayThree(input)

        result = day_one.part_two()

        expect(result).to(equal(0))
