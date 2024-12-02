import pytest
from expects import equal, expect

from src.day_one import DayOne


class TestDayOne:
    @pytest.fixture
    def input(self) -> list[str]:
        return open("inputs/01.in").read().strip().split("\n")

    def test_part_one(self, input: list[str]) -> None:
        day_one = DayOne(input)

        result = day_one.part_one()

        expect(result).to(equal(3574690))

    def test_part_two(self, input: list[str]) -> None:
        day_one = DayOne(input)

        result = day_one.part_two()

        expect(result).to(equal(22565391))
