from app import App
import time

def main():
    app = App()
    app.read_file()
    start = time.time()
    app.get_hydrogen_count()
    end = time.time()
    print(f"Tempo de execução: {((end - start) * 1000):.2f}ms\n")
    #print("Grafo: " + "\n")
    #app.show_digraph()

if __name__ == "__main__":
    main()
