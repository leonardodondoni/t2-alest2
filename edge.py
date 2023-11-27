from vertex import Vertex

class Edge:
    def __init__(self, frm: Vertex, to: Vertex, weight: int):
        self.from_vertex = frm
        self.to_vertex = to
        self.weight = weight

    def get_from(self) -> Vertex:
        return self.from_vertex

    def get_to(self) -> Vertex:
        return self.to_vertex

    def get_weight(self) -> int:
        return self.weight

    def __str__(self) -> str:
        return str(self.from_vertex) + " -> " + str(self.to_vertex) + " [label=" + str(self.weight) + "]"
