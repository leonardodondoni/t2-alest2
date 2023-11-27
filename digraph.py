from typing import List
from vertex import Vertex
from edge import Edge

class Digraph:
    NEWLINE = "\n"

    def __init__(self):
        self.adj_list = {}
        self.hydrogen = None
        self.hydrogen_read = False

    def add_edge(self, frm: Vertex, to: Vertex, weight: int) -> None:
        self.adj_list.setdefault(frm, []).append(Edge(frm, to, weight))

    def get_edges(self, vertex: Vertex) -> List[Edge]:
        return self.adj_list.get(vertex, [])

    def load_from_file(self, filename: str) -> None:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split("->")
                frm_parts = parts[0].strip().split(" ")
                to_parts = parts[1].strip().split(" ")

                for i in range(0, len(frm_parts), 2):
                    frm_weight = int(frm_parts[i])
                    frm_vertex = Vertex(frm_parts[i + 1])

                    if not self.hydrogen_read and frm_vertex.get_name() == "hidrogenio":
                        self.hydrogen = frm_vertex
                        self.hydrogen_read = True

                    to_weight = int(to_parts[0])
                    to_vertex = Vertex(to_parts[1])

                    self.add_edge(frm_vertex, to_vertex, frm_weight * to_weight)

    def get_hydrogen(self) -> Vertex:
        return self.hydrogen

    def __str__(self) -> str:
        sb = []
        sb.append("digraph {" + self.NEWLINE)
        sb.append("rankdir = LR;" + self.NEWLINE)
        sb.append("node [shape = circle];" + self.NEWLINE)

        for vertex, edges in self.adj_list.items():
            for edge in edges:
                sb.append(str(edge) + '\n')

        sb.append("}" + self.NEWLINE)
        return ''.join(sb)
