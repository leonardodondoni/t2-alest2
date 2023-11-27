class Vertex:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Vertex):
            return False
        return self.name == other.name
