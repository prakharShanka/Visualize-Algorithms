def tsp_nearest_neighbor(graph, start):
    unvisited = set(graph.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    total_distance = 0

    print(f"Starting TSP from {start}")

    while unvisited:
        # Filter out neighbors that are not in the graph or cannot be accessed from the current node
        accessible_neighbors = {node: graph[current][node] for node in unvisited if node in graph[current]}

        if not accessible_neighbors:
            print(f"No accessible neighbors from {current}. Trying to find another path.")
            # Try to connect to any unvisited node
            for next_node in unvisited:
                if next_node in graph[current]:
                    print(f"Fallback: Moving from {current} to {next_node} with distance {graph[current][next_node]}")
                    total_distance += graph[current][next_node]
                    tour.append(next_node)
                    current = next_node
                    unvisited.remove(next_node)
                    break
            else:
                print(f"Unable to find a valid path from {current}. Tour incomplete.")
                return tour, float('inf')
            continue

        nearest = min(accessible_neighbors, key=accessible_neighbors.get)
        print(f"Moving from {current} to {nearest} with distance {accessible_neighbors[nearest]}")

        total_distance += accessible_neighbors[nearest]
        tour.append(nearest)
        current = nearest
        unvisited.remove(nearest)

    # Return to the start
    if start in graph[current]:
        total_distance += graph[current][start]
        tour.append(start)
    else:
        print(f"Cannot return to start {start} from {current}. Tour incomplete.")
        return tour, float('inf')

    print(f"Tour complete with total distance {total_distance}")
    return tour, total_distance
