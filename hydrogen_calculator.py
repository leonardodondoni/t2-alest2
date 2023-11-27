from digraph import Digraph
from vertex import Vertex
from typing import Dict

class HydrogenCalculator:
    def __init__(self, graph: Digraph):
        self.hydrogen_count: Dict[Vertex, int] = {}
        self.visited = set()
        self.graph = graph

    def sum_product(self, start: Vertex) -> int:
        if start in self.hydrogen_count:
            return self.hydrogen_count[start]

        if not self.graph.get_edges(start):
            self.hydrogen_count[start] = 1
            return 1

        self.visited.add(start)
        result = 0

        for edge in self.graph.get_edges(start):
            if edge.get_to() not in self.visited:
                subtree_result = edge.get_weight() * self.sum_product(edge.get_to())
                result += subtree_result

        self.hydrogen_count[start] = result

        self.visited.remove(start)
        return result

    def get_hydrogen_count(self) -> Dict[Vertex, int]:
        return self.hydrogen_count
