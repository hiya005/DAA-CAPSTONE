
from algorithms.dijkstra import graph, dijkstra, get_path
from algorithms.tsp import nearest_neighbor
from parcel import parcels
from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack


# Step 1: Select parcels using Phase 2
sorted_parcels = merge_sort(parcels)

selected, total_value, dp = knapsack(
    sorted_parcels, 20
)

# Step 2: Get unique delivery destinations
destinations = list(
    dict.fromkeys(p.destination for p in selected)
)

print("===== SELECTED PARCELS =====")

for p in selected:
    print(p.parcel_id, "-", p.destination)


# Step 3: Run Dijkstra
print("\n===== DIJKSTRA SHORTEST PATHS =====")

distances, previous = dijkstra(graph, "Warehouse")

for location in graph:
    path = get_path(previous, location)

    print(
        "Warehouse to", location,
        ":", distances[location], "km",
        "| Path:", " -> ".join(path)
    )


# Step 4: Run Nearest Neighbor TSP
print("\n===== DELIVERY ROUTE =====")

route, total_distance, legs = nearest_neighbor(
    graph,
    "Warehouse",
    destinations
)

for leg in legs:
    print(
        leg["from"], "->", leg["to"],
        "| Distance:", leg["distance"], "km",
        "| Actual path:", " -> ".join(leg["path"])
    )


# Step 5: Final results
print("\n===== FINAL COURIER PLAN =====")

print("Route:", " -> ".join(route))
print("Total Distance:", total_distance, "km")
print("Selected Parcels:", len(selected))
print("Total Parcel Weight:",
      sum(p.weight for p in selected), "kg")
print("Total Delivery Value: Rs.", total_value)
