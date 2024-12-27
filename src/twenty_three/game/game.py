from dataclasses import dataclass


@dataclass
class Play:
    red: int
    blue: int
    green: int

    def is_invalid(self) -> bool:
        return self.red > 12 or self.green > 13 or self.blue > 14


@dataclass
class Game:
    id: int
    plays: list[Play]

    def is_valid(self) -> bool:
        for play in self.plays:
            if play.is_invalid():
                return False
        return True

    @property
    def _max_red(self) -> int:
        max_value = 0
        for play in self.plays:
            max_value = max(play.red, max_value)
        return max_value

    @property
    def _max_green(self) -> int:
        max_value = 0
        for play in self.plays:
            max_value = max(play.green, max_value)
        return max_value

    @property
    def _max_blue(self) -> int:
        max_value = 0
        for play in self.plays:
            max_value = max(play.blue, max_value)
        return max_value

    @property
    def score(self) -> int:
        return self._max_red * self._max_green * self._max_blue
