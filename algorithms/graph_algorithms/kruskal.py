def kruskal(graph):
    edges = [
        (weight, frm, to)
        for frm, adj in graph.items()
        for to, weight in adj.items()
    ]
    edges.sort()

    parent = {}
    rank = {}

    def find(node):
        if parent[node] == node:
            return node
        parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    mst = []
    for node in graph:
        parent[node] = node
        rank[node] = 0

    for weight, frm, to in edges:
        if find(frm) != find(to):
            union(frm, to)
            mst.append((frm, to, weight))

    return mst
