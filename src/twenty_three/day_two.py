from collections import defaultdict

from src.twenty_three.game.game import Game, Play


class DayTwo:
    def __init__(self, input: list[str]) -> None:
        self.games = self._parse_input(input)

    def part_one(self) -> int:
        total = 0
        for game in self.games:
            if game.is_valid():
                total += game.id
        return total

    def part_two(self) -> int:
        total = 0
        for game in self.games:
            total += game.score
        return total

    def _parse_input(self, input: list[str]) -> list[Game]:
        games: list[Game] = []
        for idx, line in enumerate(input):
            id, parts = line.split(": ")
            game_id = idx + 1
            plays: list[Play] = []
            for bag in parts.split("; "):
                _play: dict[str, int] = defaultdict(int)
                for c in bag.split(", "):
                    times, name = c.split(" ")
                    _play[name] += int(times)
                play = Play(red=_play["red"], green=_play["green"], blue=_play["blue"])
                plays.append(play)
            game = Game(game_id, plays)
            games.append(game)
        return games
