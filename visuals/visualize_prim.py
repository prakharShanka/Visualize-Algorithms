import matplotlib.pyplot as plt
import networkx as nx
from graph_algorithms.prims import prim

def visualize_prim(graph, start):
    G = nx.Graph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 9))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(f"Prim's Algorithm Visualization Starting from Vertex {start}")
    plt.show(block=False)

    mst = prim(graph, start)
    for edge in mst:
        frm, to, weight = edge
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        nx.draw_networkx_edges(G, pos, edgelist=[(frm, to)], edge_color='orange', width=2.5)
        plt.pause(1)
        plt.clf()

    nx.draw(G, pos, with_labels=True, node_color='orange', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(f"Minimum Spanning Tree (Prim's) Starting from {start}")
    plt.show()
