from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from visuals.visualize import visualize_sorting
from visuals.visualize_graph import visualize_bfs, visualize_dfs
from visuals.visualize_dijkstra import visualize_dijkstra
from visuals.visualize_prim import visualize_prim  # Import Prim's visualization
from visuals.visualize_kruskal import visualize_kruskal  # Import Kruskal's visualization
from visuals.visualize_tsp import visualize_tsp  # Import TSP visualization

class SortingVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Visualizer")
        
        # Set the default window size
        self.root.geometry("800x600")  # Set width to 800 and height to 600

        self.algorithm_name = tk.StringVar()
        self.algorithms = [
            'Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 
            'BFS', 'DFS', 'Dijkstra', 'Prim', 'Kruskal', 'TSP'
        ]
        self.selected_algorithm = self.algorithms[0]

        self.array_size = tk.IntVar(value=20)
        self.speed = tk.DoubleVar(value=1.0)

        # Full path to the background image
        image_path = r"D:\RAEES\STUDIES\Projects\SDE projects for resume\Visualization\gui\WIN_20221121_09_51_45_Pro.JPG"

        # Load the image using Pillow
        image = Image.open(image_path)
        self.background_image = ImageTk.PhotoImage(image)

        # Display the background image
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Create dropdown menu for selecting the algorithm
        ttk.Label(root, text="Choose Algorithm:", background="lightblue").pack(pady=10)
        self.dropdown = ttk.Combobox(root, textvariable=self.algorithm_name, values=self.algorithms)
        self.dropdown.pack(pady=10)
        self.dropdown.current(0)  # Default to first algorithm

        # Slider to select array size
        ttk.Label(root, text="Select Array Size:", background="lightblue").pack(pady=10)
        self.array_slider = tk.Scale(root, from_=10, to=100, orient=tk.HORIZONTAL, variable=self.array_size)
        self.array_slider.pack(pady=10)

        # Slider to control the speed of the visualization
        ttk.Label(root, text="Visualization Speed:", background="lightblue").pack(pady=10)
        self.speed_slider = tk.Scale(root, from_=0.1, to=100.0, orient=tk.HORIZONTAL, variable=self.speed, resolution=0.1)
        self.speed_slider.pack(pady=10)

        # Visualize Button
        self.visualize_button = ttk.Button(root, text="Visualize", command=self.visualize)
        self.visualize_button.pack(pady=20)

    def visualize(self):
        algorithm = self.algorithm_name.get()

        # Example weighted graph for Dijkstra, Prim, Kruskal, and TSP algorithms
        weighted_graph = {
            'A': {'B': 3, 'C': 8, 'D': 5, 'E': 7, 'F': 14, 'G': 10, 'H': 11},
            'B': {'A': 3, 'C': 6, 'D': 9, 'E': 12, 'F': 7, 'G': 13, 'H': 8},
            'C': {'A': 8, 'B': 6, 'D': 7, 'E': 8, 'F': 5, 'G': 6, 'H': 9},
            'D': {'A': 5, 'B': 9, 'C': 7, 'E': 4, 'F': 8, 'G': 7, 'H': 6},
            'E': {'A': 7, 'B': 12, 'C': 8, 'D': 4, 'F': 9, 'G': 3, 'H': 10},
            'F': {'A': 14, 'B': 7, 'C': 5, 'D': 8, 'E': 9, 'G': 2, 'H': 3},
            'G': {'A': 10, 'B': 13, 'C': 6, 'D': 7, 'E': 3, 'F': 2, 'H': 4},
            'H': {'A': 11, 'B': 8, 'C': 9, 'D': 6, 'E': 10, 'F': 3, 'G': 4}
        }

        # Existing complex graph for BFS and DFS
        complex_graph = {
            'A': ['B', 'C', 'D'],
            'B': ['A', 'E', 'F'],
            'C': ['A', 'G'],
            'D': ['A', 'H'],
            'E': ['B', 'I', 'J'],
            'F': ['B', 'K'],
            'G': ['C'],
            'H': ['D', 'L'],
            'I': ['E'],
            'J': ['E'],
            'K': ['F'],
            'L': ['H'],
            'M': ['I', 'N'],
            'N': ['I', 'J', 'M', 'O'],
            'O': ['J', 'K', 'N', 'P'],
            'P': ['K', 'L', 'O'],
        }

        if algorithm in ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort']:
            visualize_sorting(algorithm, self.array_size.get(), self.speed.get())
        elif algorithm == 'BFS':
            visualize_bfs(complex_graph, 'A')
        elif algorithm == 'DFS':
            visualize_dfs(complex_graph, 'A')
        elif algorithm == 'Dijkstra':
            visualize_dijkstra(weighted_graph, 'A')
        elif algorithm == 'Prim':
            visualize_prim(weighted_graph, 'A')
        elif algorithm == 'Kruskal':
            visualize_kruskal(weighted_graph)
        elif algorithm == 'TSP':
            visualize_tsp(weighted_graph, 'A')

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizerApp(root)
    root.mainloop()
