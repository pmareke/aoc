from collections import defaultdict


class DayTwentyThree:
    def __init__(self, input: str) -> None:
        self.input = input

    def part_one(self) -> int:
        nodes = self._get_nodes()
        networks: set[tuple] = set()
        for node in nodes:
            self._search(nodes, node, {node}, networks)
        total = 0
        for network in filter(lambda x: len(x) == 3, networks):
            if any(node.startswith("t") for node in network):
                total += 1
        return total

    def part_two(self) -> str:
        nodes = self._get_nodes()
        networks: set[tuple] = set()
        for node in nodes:
            self._search(nodes, node, {node}, networks)
        higher_network = max(networks, key=lambda network: len(network))
        return ",".join(higher_network)

    def _get_nodes(self) -> dict:
        nodes = defaultdict(list)
        for pair in self.input.split("\n"):
            x, y = pair.split("-")
            nodes[x].append(y)
            nodes[y].append(x)
        return nodes

    def _search(
        self, nodes: dict, node: str, existig_in_network: set, networks: set
    ) -> None:
        network = tuple(sorted(existig_in_network))
        if network in networks:
            return
        networks.add(network)
        for _node in nodes[node]:
            if _node in existig_in_network:
                continue
            if not all(_node in nodes[n] for n in existig_in_network):
                continue
            self._search(nodes, _node, {*existig_in_network, _node}, networks)
