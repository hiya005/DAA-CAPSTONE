import time
import random
import csv
import os
import statistics
import matplotlib.pyplot as plt

from parcel import Parcel, parcels
from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import graph, dijkstra
from algorithms.tsp import nearest_neighbor


def measure_time(function, repeats=10):

    times = []

    for _ in range(repeats):
        start = time.perf_counter()
        function()
        end = time.perf_counter()

        times.append(end - start)

    return statistics.median(times) * 1000


def generate_parcels(size):

    destinations = ["A", "B", "C", "D", "E", "F"]

    return [
        Parcel(
            f"P{i}",
            random.choice(destinations),
            random.randint(1, 10),
            random.randint(1, 5),
            random.randint(1, 10),
            random.randint(100, 1000)
        )
        for i in range(size)
    ]


def run_performance_tests():

    sizes = [8, 50, 100, 200]

    results = {
        "size": [],
        "merge_sort": [],
        "knapsack": [],
        "dijkstra": [],
        "tsp": []
    }

    print("===== PERFORMANCE TESTING =====")

    for size in sizes:

        test_data = generate_parcels(size)

        capacity = max(20, size)

        # Measure Merge Sort
        sort_time = measure_time(
            lambda: merge_sort(test_data.copy())
        )

        # Measure Knapsack
        sorted_data = merge_sort(test_data)

        knapsack_time = measure_time(
            lambda: knapsack(sorted_data, capacity),
            repeats=5
        )

        # Measure Dijkstra
        dijkstra_time = measure_time(
            lambda: dijkstra(graph, "Warehouse")
        )

        # Measure TSP
        destinations = list("ABCDEF")

        tsp_time = measure_time(
            lambda: nearest_neighbor(
                graph, "Warehouse", destinations
            )
        )

        results["size"].append(size)
        results["merge_sort"].append(sort_time)
        results["knapsack"].append(knapsack_time)
        results["dijkstra"].append(dijkstra_time)
        results["tsp"].append(tsp_time)

        print(f"\nDataset Size: {size}")

        print(f"Merge Sort: {sort_time:.6f} ms")
        print(f"Knapsack: {knapsack_time:.6f} ms")
        print(f"Dijkstra: {dijkstra_time:.6f} ms")
        print(f"TSP: {tsp_time:.6f} ms")

    return results


def save_results(results):

    os.makedirs("results", exist_ok=True)

    with open(
        "results/performance_results.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Dataset Size",
            "Merge Sort (ms)",
            "Knapsack (ms)",
            "Dijkstra (ms)",
            "TSP (ms)"
        ])

        for i in range(len(results["size"])):

            writer.writerow([
                results["size"][i],
                results["merge_sort"][i],
                results["knapsack"][i],
                results["dijkstra"][i],
                results["tsp"][i]
            ])


def generate_chart(results):

    plt.figure(figsize=(10, 6))

    for algorithm in [
        "merge_sort",
        "knapsack",
        "dijkstra",
        "tsp"
    ]:

        plt.plot(
            results["size"],
            results[algorithm],
            marker="o",
            label=algorithm.replace("_", " ").title()
        )

    plt.xlabel("Number of Parcels")
    plt.ylabel("Execution Time (milliseconds)")
    plt.title("Algorithm Performance Comparison")

    plt.legend()
    plt.grid(True)

    plt.savefig("results/performance_chart.png")
    plt.show()


def generate_graph(size):
    """Generate a connected weighted undirected graph."""

    graph_data = {
        f"N{i}": [] for i in range(size)
    }

    # Connect consecutive nodes to ensure connectivity
    for i in range(size - 1):
        a = f"N{i}"
        b = f"N{i + 1}"
        weight = random.randint(1, 10)

        graph_data[a].append((b, weight))
        graph_data[b].append((a, weight))

    # Add additional random roads
    for _ in range(size * 2):
        a = random.randint(0, size - 1)
        b = random.randint(0, size - 1)

        if a != b:
            weight = random.randint(1, 10)

            graph_data[f"N{a}"].append(
                (f"N{b}", weight)
            )
            graph_data[f"N{b}"].append(
                (f"N{a}", weight)
            )

    return graph_data


def test_graph_performance():

    sizes = [10, 25, 50, 100]

    graph_results = {
        "size": [],
        "dijkstra": [],
        "tsp": []
    }

    print("\n===== GRAPH PERFORMANCE TESTING =====")

    for size in sizes:

        test_graph = generate_graph(size)

        start = "N0"

        destinations = [
            f"N{i}" for i in range(1, min(size, 21))
        ]

        # Measure Dijkstra
        dijkstra_time = measure_time(
            lambda: dijkstra(test_graph, start)
        )

        # Measure TSP
        tsp_time = measure_time(
            lambda: nearest_neighbor(
                test_graph, start, destinations
            ),
            repeats=5
        )

        graph_results["size"].append(size)
        graph_results["dijkstra"].append(dijkstra_time)
        graph_results["tsp"].append(tsp_time)

        print(f"\nGraph Size: {size} vertices")
        print(f"Dijkstra: {dijkstra_time:.6f} ms")
        print(f"TSP: {tsp_time:.6f} ms")

    # Save graph performance chart
    plt.figure(figsize=(9, 5))

    plt.plot(
        graph_results["size"],
        graph_results["dijkstra"],
        marker="o",
        label="Dijkstra"
    )

    plt.plot(
        graph_results["size"],
        graph_results["tsp"],
        marker="o",
        label="Nearest Neighbor TSP"
    )

    plt.xlabel("Number of Graph Vertices")
    plt.ylabel("Execution Time (milliseconds)")
    plt.title("Graph Algorithm Performance")

    plt.legend()
    plt.grid(True)

    plt.savefig("results/graph_performance_chart.png")
    plt.show()

    print("\nGraph performance testing completed!")

if __name__ == "__main__":

    results = run_performance_tests()

    save_results(results)

    generate_chart(results)

    test_graph_performance()