from digraph import Digraph
from hydrogen_calculator import HydrogenCalculator

class App:
    def __init__(self):
        self.g = Digraph()

    def read_file(self):
        try:
            self.g.load_from_file("cases/z350.txt")
        except Exception as e:
            print("Erro ao ler o arquivo.")

    def show_digraph(self):
        print(self.g.__str__())

    def get_hydrogen_count(self):
        start = self.g.get_hydrogen()
        hc = HydrogenCalculator(self.g)
        result = hc.sum_product(start)
        print("Hidrogênios: " + str(result))
