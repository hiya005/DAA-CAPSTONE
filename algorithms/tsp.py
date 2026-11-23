
from algorithms.dijkstra import dijkstra, get_path


def nearest_neighbor(graph, start, destinations):

    # Remove duplicate destinations
    destinations = list(dict.fromkeys(destinations))

    # Calculate shortest paths from every required location
    all_distances = {}
    all_previous = {}

    locations = [start] + destinations

    for location in locations:
        distances, previous = dijkstra(graph, location)

        all_distances[location] = distances
        all_previous[location] = previous

    route = [start]
    unvisited = destinations.copy()

    current = start
    total_distance = 0
    legs = []

    # Visit the nearest unvisited destination
    while unvisited:

        next_location = min(
            unvisited,
            key=lambda node: all_distances[current][node]
        )

        distance = all_distances[current][next_location]

        path = get_path(
            all_previous[current],
            next_location
        )

        legs.append({
            "from": current,
            "to": next_location,
            "distance": distance,
            "path": path
        })

        total_distance += distance
        route.append(next_location)

        unvisited.remove(next_location)
        current = next_location

    # Return to the warehouse
    return_distance = all_distances[current][start]
    return_path = get_path(
        all_previous[current],
        start
    )

    legs.append({
        "from": current,
        "to": start,
        "distance": return_distance,
        "path": return_path
    })

    total_distance += return_distance
    route.append(start)

    return route, total_distance, legs
