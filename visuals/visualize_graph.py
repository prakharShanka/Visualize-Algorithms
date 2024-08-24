import matplotlib.pyplot as plt
import networkx as nx
from graph_algorithms.bfs import bfs
from graph_algorithms.dfs import dfs

def visualize_bfs(graph, start):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)  # Spring layout for better visualization in complex graphs
    bfs_order = bfs(graph, start)

    plt.figure(figsize=(12, 9))  # Adjust the figure size for larger graphs
    for i, node in enumerate(bfs_order):
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        nx.draw_networkx_nodes(G, pos, nodelist=bfs_order[:i+1], node_color='orange')
        plt.title(f"BFS Visualization Starting from Vertex {start}")
        plt.pause(1)  # Pause for visualization
        plt.clf()  # Clear the plot for the next iteration

    nx.draw(G, pos, with_labels=True, node_color='orange', edge_color='gray')
    plt.title(f"BFS Visualization Complete Starting from Vertex {start}")
    plt.show()

def visualize_dfs(graph, start):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    dfs_order = dfs(graph, start)

    plt.figure(figsize=(12, 9))  # Adjust the figure size for larger graphs
    for i, node in enumerate(dfs_order):
        nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='gray')
        nx.draw_networkx_nodes(G, pos, nodelist=dfs_order[:i+1], node_color='red')
        plt.title(f"DFS Visualization Starting from Vertex {start}")
        plt.pause(1)  # Pause for visualization
        plt.clf()  # Clear the plot for the next iteration

    nx.draw(G, pos, with_labels=True, node_color='red', edge_color='gray')
    plt.title(f"DFS Visualization Complete Starting from Vertex {start}")
    plt.show()
