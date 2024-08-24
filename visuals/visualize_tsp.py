import matplotlib.pyplot as plt
import networkx as nx
from graph_algorithms.tsp import tsp_nearest_neighbor

def visualize_tsp(graph, start):
    G = nx.Graph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots(figsize=(12, 9))

    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', ax=ax)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    plt.title(f"TSP Visualization Starting from Vertex {start}")
    plt.draw()  # Draw the initial plot
    plt.pause(2)  # Pause to allow the initial plot to render

    tour, total_distance = tsp_nearest_neighbor(graph, start)

    for i in range(len(tour) - 1):
        frm, to = tour[i], tour[i + 1]
        # Highlight the current edge being added to the tour
        nx.draw_networkx_edges(G, pos, edgelist=[(frm, to)], edge_color='orange', width=2.5, ax=ax)
        plt.title(f"TSP Visualization - Step {i + 1}")
        plt.draw()  # Update the plot
        plt.pause(1)  # Pause to visualize the step

    # Final tour visualization
    plt.title(f"TSP Tour Complete - Total Distance: {total_distance}")
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Keep the plot open
