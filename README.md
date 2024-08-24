# Algorithm Visualization Project

This project provides a visual representation of various algorithms, including sorting algorithms and graph-based algorithms like BFS, DFS, Dijkstra's algorithm, Kruskal's algorithm, and more. It also includes a graphical user interface (GUI) for interactive exploration of these algorithms.

## Project Structure

- **LICENSE**: Contains the licensing information for the project.
- **README.md**: Overview of the project and instructions on how to use it.
- **requirements.txt**: Lists the Python libraries required to run the project.

### Directories:
- **algorithms/**: Contains scripts implementing various algorithms.
  - **sorting_algorithms.py**: Sorting algorithms.
  - **graph_algorithms/**: Scripts for BFS, DFS, Dijkstra, Kruskal, Prim, and TSP algorithms.
- **visuals/**: Visualization scripts for the algorithms.
- **gui/**: Graphical user interface for interacting with the visualizations.
- **virtualenv/**: (Excluded) Python virtual environment.

## Requirements

This project requires the following Python libraries, which can be installed using the `requirements.txt` file:
- matplotlib
- networkx
- numpy
- PyQt5

## Installation

1. Clone the repository to your local machine.
2. Set up a virtual environment (optional) and activate it.
3. Install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the GUI script to interact with the algorithm visualizations:

```bash
python gui/gui.py
```

2. Explore different algorithms through the provided interface.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
