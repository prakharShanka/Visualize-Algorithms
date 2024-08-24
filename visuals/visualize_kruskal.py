import matplotlib.pyplot as plt
import networkx as nx
from graph_algorithms.kruskal import kruskal

def visualize_kruskal(graph):
    G = nx.Graph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 9))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(f"Kruskal's Algorithm Visualization")
    plt.show(block=False)

    mst = kruskal(graph)
    for edge in mst:
        frm, to, weight = edge
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        nx.draw_networkx_edges(G, pos, edgelist=[(frm, to)], edge_color='orange', width=2.5)
        plt.pause(1)
        plt.clf()

    nx.draw(G, pos, with_labels=True, node_color='orange', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(f"Minimum Spanning Tree (Kruskal's)")
    plt.show()
