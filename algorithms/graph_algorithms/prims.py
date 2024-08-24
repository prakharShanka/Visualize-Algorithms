import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [
        (weight, start, to)
        for to, weight in graph[start].items()
    ]
    heapq.heapify(edges)

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))

            for to_next, weight in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (weight, to, to_next))

    return mst
