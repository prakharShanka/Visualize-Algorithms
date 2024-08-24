from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    
    return order
