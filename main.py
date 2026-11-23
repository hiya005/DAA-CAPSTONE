
from parcel import parcels
from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import graph, dijkstra, get_path
from algorithms.tsp import nearest_neighbor


def display_parcels():
    print("\n===== AVAILABLE PARCELS =====")

    for p in parcels:
        print(
            f"{p.parcel_id} | Destination: {p.destination} "
            f"| Weight: {p.weight} kg "
            f"| Priority: {p.priority} "
            f"| Deadline: {p.deadline} days "
            f"| Value: Rs. {p.value}"
        )


def run_courier_planner():

    print("\n===== MINI COURIER PLANNER =====")

    # Step 1: Sort parcels
    sorted_parcels = merge_sort(parcels)

    print("\n--- PRIORITIZED PARCELS ---")

    for p in sorted_parcels:
        print(
            f"{p.parcel_id} | Priority: {p.priority} "
            f"| Deadline: {p.deadline}"
        )

    # Step 2: Optimize parcel selection
    capacity = 20

    selected, total_value, dp = knapsack(
        sorted_parcels, capacity
    )

    print("\n--- SELECTED PARCELS ---")

    total_weight = 0

    for p in selected:
        print(
            f"{p.parcel_id} | Destination: {p.destination} "
            f"| Weight: {p.weight} kg "
            f"| Value: Rs. {p.value}"
        )

        total_weight += p.weight

    print("\nTotal Weight:", total_weight, "kg")
    print("Vehicle Capacity:", capacity, "kg")
    print("Maximum Delivery Value: Rs.", total_value)

    # Step 3: Find unique delivery locations
    destinations = list(
        dict.fromkeys(
            p.destination for p in selected
        )
    )

    # Step 4: Dijkstra shortest paths
    print("\n--- SHORTEST PATHS FROM WAREHOUSE ---")

    distances, previous = dijkstra(graph, "Warehouse")

    for location in destinations:
        path = get_path(previous, location)

        print(
            location, ":",
            distances[location], "km |",
            " -> ".join(path)
        )

    # Step 5: Nearest Neighbor TSP
    print("\n--- OPTIMIZED DELIVERY ROUTE ---")

    route, total_distance, legs = nearest_neighbor(
        graph,
        "Warehouse",
        destinations
    )

    for leg in legs:
        print(
            leg["from"], "->", leg["to"],
            "| Distance:", leg["distance"], "km",
            "| Road Path:", " -> ".join(leg["path"])
        )

    # Step 6: Final summary
    print("\n========== FINAL COURIER SUMMARY ==========")

    print("Selected Parcels:", len(selected))
    print("Total Weight:", total_weight, "kg")
    print("Delivery Value: Rs.", total_value)
    print("Delivery Locations:", len(destinations))
    print("Final Route:", " -> ".join(route))
    print("Total Travel Distance:", total_distance, "km")

    print("===========================================")


def find_shortest_path():

    start = input("\nEnter starting location: ").strip()
    destination = input("Enter destination: ").strip()

    if start not in graph or destination not in graph:
        print("Invalid location. Please try again.")
        return

    distances, previous = dijkstra(graph, start)

    path = get_path(previous, destination)

    print("\nShortest Path:", " -> ".join(path))
    print("Total Distance:", distances[destination], "km")


def main():

    while True:

        print("\n================================")
        print("       MINI COURIER PLANNER")
        print("================================")
        print("1. View All Parcels")
        print("2. Generate Courier Delivery Plan")
        print("3. Find Shortest Path")
        print("4. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_parcels()

        elif choice == "2":
            run_courier_planner()

        elif choice == "3":
            find_shortest_path()

        elif choice == "4":
            print("Thank you for using Mini Courier Planner!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
