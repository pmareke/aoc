from collections import defaultdict


class DayTwentyThree:
    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        nodes = self._get_nodes()
        sets: set[tuple] = set()
        for node in nodes:
            self._search(nodes, node, {node}, sets)
        total = 0
        for s in filter(lambda x: len(x) == 3, sets):
            if any(c.startswith("t") for c in s):
                total += 1
        return total

    def part_two(self) -> str:
        nodes = self._get_nodes()
        sets: set[tuple] = set()
        for node in nodes:
            self._search(nodes, node, {node}, sets)

        max_set = max(sets, key=lambda x: len(x))
        return ",".join(max_set)

    def _get_nodes(self) -> dict:
        nodes = defaultdict(list)
        for pair in self.input.split("\n"):
            x, y = pair.split("-")
            nodes[x].append(y)
            nodes[y].append(x)
        return nodes

    def _search(
        self, nodes: dict, node: str, existig_in_network: set, sets: set
    ) -> None:
        key = tuple(sorted(existig_in_network))
        if key in sets:
            return
        sets.add(key)
        for _node in nodes[node]:
            if _node in existig_in_network:
                continue
            if not all(_node in nodes[query] for query in existig_in_network):
                continue
            self._search(nodes, _node, {*existig_in_network, _node}, sets)
