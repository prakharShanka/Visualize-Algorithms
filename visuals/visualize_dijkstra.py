import matplotlib.pyplot as plt
import networkx as nx
from graph_algorithms.dijkstra import dijkstra

def visualize_dijkstra(graph, start):
    G = nx.Graph()

    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    distances, shortest_path_tree = dijkstra(graph, start)

    plt.figure(figsize=(12, 9))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(f"Dijkstra's Algorithm Visualization Starting from Vertex {start}")
    plt.show(block=False)

    # Animate the process
    current_node = start
    visited_nodes = set([start])
    for neighbor in shortest_path_tree:
        visited_nodes.add(neighbor)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        path_edges = [(neighbor, shortest_path_tree[neighbor])]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='orange', width=2.5)
        nx.draw_networkx_nodes(G, pos, nodelist=list(visited_nodes), node_color='orange')
        plt.pause(1)
        plt.clf()

    # Final visualization with all paths
    nx.draw(G, pos, with_labels=True, node_color='orange', edge_color='gray')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='orange', width=2.5)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(f"Shortest Paths from {start}")
    plt.show()
