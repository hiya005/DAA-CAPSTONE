
import heapq


# Courier road network (undirected weighted graph)
graph = {
    "Warehouse": [("A", 4), ("B", 6)],
    "A": [("Warehouse", 4), ("B", 2), ("C", 5)],
    "B": [("Warehouse", 6), ("A", 2), ("C", 3), ("D", 7)],
    "C": [("A", 5), ("B", 3), ("D", 4), ("E", 6)],
    "D": [("B", 7), ("C", 4), ("E", 2), ("F", 5)],
    "E": [("C", 6), ("D", 2), ("F", 3)],
    "F": [("D", 5), ("E", 3)]
}


def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        # Ignore outdated queue entries
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, previous


def get_path(previous, destination):

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path

