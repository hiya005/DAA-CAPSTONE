# MINI-COURIER PLANNER
## Final Project Report

**Course:** Design and Analysis of Algorithms  
**Project Title:** Mini-Courier Planner  
**Programming Language:** Python  
**Project Type:** Individual Capstone Project  

---

# 1. Abstract

The Mini-Courier Planner is a Python-based application designed to simulate an intelligent courier delivery planning system. It combines sorting algorithms, dynamic programming, graph algorithms and approximation techniques to generate an efficient parcel selection and delivery plan.

The system prioritizes parcels according to their priority and delivery deadlines, selects the most valuable combination of parcels within a fixed vehicle capacity, calculates shortest paths between delivery locations and generates an approximate delivery route.

The project implements Merge Sort, 0/1 Knapsack using Dynamic Programming, Dijkstra's Shortest Path Algorithm and the Nearest Neighbor approach for the Travelling Salesperson Problem (TSP).

The application also performs runtime analysis on different dataset sizes to understand the performance of the implemented algorithms.

# 2. Introduction

Courier companies handle multiple parcels that need to be delivered to different destinations. Planning deliveries requires selecting suitable parcels, considering vehicle capacity and determining efficient routes.

Performing these tasks manually can be time-consuming and may result in inefficient resource utilization.

The Mini-Courier Planner addresses this problem by integrating different algorithmic techniques into a single application. It provides a simplified simulation of a courier planning system using a predefined parcel dataset and road network.

# 3. Problem Statement

To develop a Python application that accepts a list of parcels and delivery locations and generates an ordered delivery route along with an optimized parcel packing plan.

The system should:

- Prioritize parcels according to their priority and deadlines.
- Select parcels that maximize total delivery value within vehicle capacity.
- Calculate the shortest paths between locations.
- Generate an approximate route covering all selected delivery destinations.
- Measure the execution time of major algorithms.

# 4. Objectives

1. Implement an efficient sorting algorithm for parcel prioritization.
2. Apply Dynamic Programming to solve the 0/1 Knapsack problem.
3. Represent delivery locations using a weighted graph.
4. Implement Dijkstra's algorithm to calculate shortest paths.
5. Apply the Nearest Neighbor TSP approximation for route planning.
6. Analyze the performance of algorithms using different input sizes.
7. Develop an interactive, menu-driven Python application.

# 5. Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Python | Main programming language |
| VS Code | Development environment |
| Matplotlib | Performance visualization |
| CSV | Storing runtime results |
| Heapq | Priority queue for Dijkstra |
| Dataclasses | Defining parcel objects |

# 6. System Design and Planning (Phase 1)

## 6.1 Parcel Data Structure

Each parcel is represented using the following attributes:

| Attribute | Description |
|---|---|
| Parcel ID | Unique identification of parcel |
| Destination | Delivery location |
| Weight | Weight of parcel in kg |
| Priority | Priority level from 1 to 5 |
| Deadline | Delivery deadline in days |
| Value | Delivery value in rupees |

A Python dataclass is used to represent parcel information.

## 6.2 Sample Parcel Dataset

The system contains eight predefined parcels.

| Parcel ID | Destination | Weight (kg) | Priority | Deadline (days) | Value (₹) |
|---|---:|---:|---:|---:|---:|
| P01 | A | 5 | 4 | 2 | 500 |
| P02 | B | 8 | 5 | 1 | 800 |
| P03 | C | 4 | 3 | 3 | 400 |
| P04 | D | 7 | 5 | 2 | 700 |
| P05 | E | 3 | 2 | 4 | 300 |
| P06 | F | 6 | 4 | 1 | 600 |
| P07 | A | 2 | 3 | 2 | 250 |
| P08 | C | 9 | 1 | 5 | 350 |

The vehicle capacity is fixed at **20 kg**.

## 6.3 Road Network Representation

The delivery network is represented as an undirected weighted graph.

- Vertices represent the warehouse and delivery locations.
- Edges represent roads between locations.
- Edge weights represent road distances in kilometres.
- The Warehouse is the starting and ending location.

The graph contains seven vertices and eleven undirected edges.

### Road connections

| Connection | Distance (km) |
|---|---:|
| Warehouse – A | 4 |
| Warehouse – B | 6 |
| A – B | 2 |
| A – C | 5 |
| B – C | 3 |
| B – D | 7 |
| C – D | 4 |
| C – E | 6 |
| D – E | 2 |
| D – F | 5 |
| E – F | 3 |

The graph is stored using an adjacency list in Python.

## 6.4 Selected Algorithms

| Algorithm | Purpose |
|---|---|
| Merge Sort | Sorting parcels |
| 0/1 Knapsack | Selecting parcels within capacity |
| Dijkstra's Algorithm | Finding shortest paths |
| Nearest Neighbor TSP | Generating delivery route |

## 6.5 Overall System Workflow

1. Load the predefined parcel dataset.
2. Sort parcels according to priority and deadline.
3. Apply the Knapsack algorithm to select parcels.
4. Identify unique delivery destinations.
5. Calculate shortest paths using Dijkstra's algorithm.
6. Generate an approximate delivery route using Nearest Neighbor.
7. Display the final courier summary.

# 7. Package Prioritization and Box Filling (Phase 2)

## 7.1 Parcel Sorting Using Merge Sort

Merge Sort is implemented to prioritize parcels.

The sorting criteria are:

1. Higher priority parcels are placed first.
2. If two parcels have the same priority, the parcel with the earlier deadline is placed first.

Merge Sort follows the Divide and Conquer approach. It divides the dataset into smaller parts, sorts them and merges the sorted parts.

### Pseudocode

```text
MERGE_SORT(parcels):
    IF length(parcels) <= 1:
        RETURN parcels

    Divide parcels into left and right halves

    left = MERGE_SORT(left)
    right = MERGE_SORT(right)

    RETURN MERGE(left, right)
```

### Sorted Parcel Output

| Parcel ID | Destination | Priority | Deadline |
|---|---|---:|---:|
| P02 | B | 5 | 1 |
| P04 | D | 5 | 2 |
| P06 | F | 4 | 1 |
| P01 | A | 4 | 2 |
| P07 | A | 3 | 2 |
| P03 | C | 3 | 3 |
| P05 | E | 2 | 4 |
| P08 | C | 1 | 5 |

## 7.2 Parcel Selection Using 0/1 Knapsack

The 0/1 Knapsack algorithm is used to select parcels that maximize the total delivery value without exceeding the vehicle capacity.

Each parcel has:

- A weight.
- A value.

A parcel can either be selected completely or excluded. Partial selection is not allowed.

### Dynamic Programming Recurrence

Let:

- `DP[i][w]` represent the maximum value obtainable using the first `i` parcels with capacity `w`.
- `weight[i]` represent the parcel weight.
- `value[i]` represent the parcel value.

The recurrence is:

```text
IF weight[i] <= w:

    DP[i][w] = MAX(
        DP[i-1][w],
        value[i] + DP[i-1][w-weight[i]]
    )

ELSE:

    DP[i][w] = DP[i-1][w]
```

The DP table is constructed and backtracking is used to identify the selected parcels.

### Selected Parcels

| Parcel ID | Destination | Weight (kg) | Value (₹) |
|---|---|---:|---:|
| P04 | D | 7 | 700 |
| P06 | F | 6 | 600 |
| P01 | A | 5 | 500 |
| P07 | A | 2 | 250 |
| **Total** | | **20** | **2050** |

### Final Packing Result

- Vehicle capacity: 20 kg
- Total selected weight: 20 kg
- Total selected parcels: 4
- Maximum delivery value: ₹2,050

The selected parcels exactly utilize the available vehicle capacity.

# 8. Route Maker and Graph Processing (Phase 3)

## 8.1 Dijkstra's Shortest Path Algorithm

Dijkstra's algorithm is implemented to calculate the shortest distance from a starting location to all other reachable locations.

A priority queue is maintained using Python's `heapq` module.

The algorithm repeatedly selects the location with the smallest known distance and updates the distances of its neighboring locations.

### Pseudocode

```text
DIJKSTRA(graph, start):

    Initialize all distances as infinity
    Set distance[start] = 0

    Insert start into priority queue

    WHILE priority queue is not empty:

        Remove location with minimum distance

        FOR each neighbor:

            Calculate new distance

            IF new distance is smaller:
                Update distance
                Update previous location
                Insert neighbor into queue

    RETURN distances and previous
```

### Shortest Paths from Warehouse

| Destination | Shortest Distance | Shortest Path |
|---|---:|---|
| Warehouse | 0 km | Warehouse |
| A | 4 km | Warehouse → A |
| B | 6 km | Warehouse → B |
| C | 9 km | Warehouse → A → C |
| D | 13 km | Warehouse → B → D |
| E | 15 km | Warehouse → A → C → E |
| F | 18 km | Warehouse → B → D → F |

## 8.2 Nearest Neighbor TSP Approximation

The Travelling Salesperson Problem (TSP) involves finding a route that visits all required destinations and returns to the starting point.

Finding the exact optimal route can become computationally expensive as the number of destinations increases.

Therefore, the Nearest Neighbor heuristic is used.

The algorithm:

1. Starts from the Warehouse.
2. Finds the nearest unvisited delivery destination.
3. Moves to that destination.
4. Repeats until all selected destinations are visited.
5. Returns to the Warehouse.

Dijkstra's algorithm provides the shortest road distance between each pair of locations considered by the route planner.

### Final Delivery Destinations

The selected parcels require deliveries at:

- D
- F
- A

Destination A appears twice in the selected parcel list, so it is visited only once in the route.

### Generated Delivery Route

**Warehouse → A → D → F → Warehouse**

### Route Distance Calculation

| Route Leg | Distance | Road Path |
|---|---:|---|
| Warehouse → A | 4 km | Warehouse → A |
| A → D | 9 km | A → B → D |
| D → F | 5 km | D → F |
| F → Warehouse | 18 km | F → D → B → Warehouse |
| **Total** | **36 km** | |

The total approximate delivery route distance is **36 km**.

The Nearest Neighbor algorithm is a heuristic. It generates a practical approximate route but does not guarantee the globally shortest possible TSP route.

# 9. Performance Testing and Optimization (Phase 4)

## 9.1 Purpose of Performance Testing

Performance testing is performed to evaluate the execution time of the implemented algorithms for different input sizes.

The Python `time.perf_counter()` function is used to measure execution time.

Repeated measurements are taken, and the median execution time is used to reduce the effect of individual timing fluctuations.

## 9.2 Parcel Dataset Testing

The algorithms are tested with different parcel dataset sizes:

- 8 parcels
- 50 parcels
- 100 parcels
- 200 parcels

### Runtime Results

The following table records the measured execution times from a performance test run.

| Dataset Size | Merge Sort (ms) | Knapsack (ms) | Dijkstra (ms) | TSP (ms) |
|---:|---:|---:|---:|---:|
| 8 | 0.0164 | 0.0530 | 0.0062 | 0.0480 |
| 50 | 0.1135 | 0.3350 | 0.0037 | 0.0310 |
| 100 | 0.2207 | 2.0800 | 0.0042 | 0.0400 |
| 200 | 0.3675 | 7.4100 | 0.0035 | 0.0310 |

*Note: Runtime values are approximate and may vary depending on hardware, system load and execution conditions.*

## 9.3 Graph Performance Testing

An additional experiment is performed using generated graphs of different sizes.

The graph sizes tested are:

- 10 vertices
- 25 vertices
- 50 vertices
- 100 vertices

The graph experiment measures Dijkstra's algorithm and Nearest Neighbor route planning on larger generated road networks.

A separate performance chart is generated and saved as:

`results/graph_performance_chart.png`

## 9.4 Performance Observations

1. Merge Sort demonstrates efficient sorting performance as the parcel dataset increases.
2. Knapsack execution time increases with the number of parcels and the selected capacity because it uses a two-dimensional Dynamic Programming table.
3. Dijkstra's algorithm uses a priority queue to efficiently calculate shortest paths.
4. Nearest Neighbor provides a practical approximate delivery route without exhaustively evaluating every possible route.
5. Execution time depends on input size, graph structure and available system resources.

**Important observation:** In the parcel performance experiment, Dijkstra and TSP use the same predefined road graph for each parcel dataset size. Therefore, their nearly constant timings in that experiment do not demonstrate graph-size scaling. The additional graph experiment evaluates their behavior on generated graphs of increasing size.

## 9.5 Possible Optimizations

The following improvements can be considered in future versions:

- Use more advanced route optimization methods to improve the approximate TSP solution.
- Use more efficient memory management for large Knapsack DP tables.
- Reduce repeated shortest-path calculations by caching previously calculated distances.
- Introduce real-world road distance and traffic information.
- Support multiple vehicles and delivery trips.

# 10. Implementation and Application Features (Phase 5)

The complete application is developed using Python and divided into separate modules for better code organization and maintainability.

### Application Menu

The application provides four options:

1. View All Parcels
2. Generate Courier Delivery Plan
3. Find Shortest Path
4. Exit

### Main Application Output

The final courier plan produces the following result:

| Parameter | Result |
|---|---|
| Selected Parcels | 4 |
| Total Weight | 20 kg |
| Vehicle Capacity | 20 kg |
| Delivery Value | ₹2,050 |
| Delivery Locations | 3 |
| Final Route | Warehouse → A → D → F → Warehouse |
| Total Travel Distance | 36 km |

### Project Directory Structure

```text
Mini-Courier-Planner/
│
├── algorithms/
│   ├── __init__.py
│   ├── sorting.py
│   ├── knapsack.py
│   ├── dijkstra.py
│   └── tsp.py
│
├── data/
│
├── docs/
│   ├── Final_Report.md
│   ├── phase2_sorting_knapsack.png
│   ├── phase3_dijkstra_tsp_route.png
│   └── phase4_performance_testing.png
│
├── results/
│   ├── performance_results.csv
│   ├── performance_chart.png
│   └── graph_performance_chart.png
│
├── main.py
├── parcel.py
├── performance.py
├── test_phase2.py
├── test_phase3.py
├── README.md
└── requirements.txt
```

# 11. Time and Space Complexity Analysis

Let:

- `n` = number of parcels.
- `W` = vehicle capacity.
- `V` = number of graph vertices.
- `E` = number of graph edges.
- `k` = number of unique delivery destinations.

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| Merge Sort | O(n log n) | O(n) |
| 0/1 Knapsack DP | O(nW) | O(nW) |
| Dijkstra using a binary heap | O((V + E) log V) | O(V + E) |
| Nearest Neighbor with pairwise Dijkstra | O((k + 1)(V + E) log V + k²) | O(kV + V + E) |

The Knapsack complexity depends on both the number of parcels and the vehicle capacity.

The route planner calculates shortest-path information from the starting location and delivery destinations before selecting the nearest unvisited destination.

# 12. Testing and Verification

The project is tested using separate test files and the main application.

| Test Case | Expected Result | Status |
|---|---|---|
| Display all parcels | Display all predefined parcels | Passed |
| Sort parcels | Sort by priority and deadline | Passed |
| Knapsack selection | Select parcels within 20 kg capacity | Passed |
| Dijkstra | Calculate shortest paths | Passed |
| TSP approximation | Generate delivery route | Passed |
| Find shortest path | Accept valid locations and display shortest route | Passed |
| Invalid location | Display an error message | Implemented |
| Exit application | Terminate the application | Passed |
| Performance testing | Generate runtime measurements and charts | Executed |

### Execution Instructions

**Step 1:** Open the project folder in VS Code.

**Step 2:** Install the required dependency:

```powershell
pip install -r requirements.txt
```

**Step 3:** Run the main application:

```powershell
python main.py
```

**Step 4:** Select an option from the application menu.

**Step 5:** To execute performance testing, run:

```powershell
python performance.py
```

The performance results and charts are saved in the `results` folder.

# 13. Limitations

- The project uses a predefined parcel dataset.
- The road network and distances are simulated.
- Vehicle capacity is fixed at 20 kg.
- The system handles one delivery trip at a time.
- Nearest Neighbor provides an approximate route rather than a guaranteed globally optimal route.
- Runtime measurements may differ across systems.

# 14. Future Scope

The project can be improved by introducing:

1. Dynamic parcel entry and deletion.
2. Multiple delivery vehicles with different capacities.
3. Real-world maps and road distances.
4. Traffic-aware route planning.
5. A graphical user interface.
6. More advanced TSP optimization techniques.
7. Database integration for storing parcel and delivery information.

# 15. Conclusion

The Mini-Courier Planner successfully demonstrates the integration of multiple Design and Analysis of Algorithms concepts into a practical application.

Merge Sort is used to prioritize parcels, while 0/1 Knapsack using Dynamic Programming selects a combination of parcels that maximizes delivery value within the available vehicle capacity.

Dijkstra's algorithm calculates the shortest paths between delivery locations, and the Nearest Neighbor heuristic generates an approximate overall delivery route.

The final application successfully selects four parcels with a total weight of 20 kg and a delivery value of ₹2,050. It generates the route Warehouse → A → D → F → Warehouse, with a total distance of 36 km.

Performance testing is also conducted using different parcel dataset sizes and generated graph sizes.

Overall, the project demonstrates how sorting, dynamic programming, graph algorithms and approximation techniques can be combined to solve a real-world-inspired courier planning problem.

---

