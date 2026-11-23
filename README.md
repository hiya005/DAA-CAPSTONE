# Mini-Courier-Planner

## Project Overview

Mini-Courier-Planner is a Python-based courier planning application that prioritizes parcels, selects an optimal combination of parcels based on vehicle capacity, calculates shortest delivery paths and generates an efficient delivery route.

The project integrates Sorting, Dynamic Programming, Graph Algorithms and Approximation Techniques.

## Objectives

- Prioritize parcels according to priority and delivery deadlines.
- Select parcels that maximize total delivery value within vehicle capacity.
- Calculate shortest paths between delivery locations.
- Generate an efficient delivery route using the Nearest Neighbor TSP approximation.
- Analyze the execution time of different algorithms.

## Technologies Used

- Python
- Matplotlib
- CSV
- Python Heap Queue (`heapq`)
- VS Code

## Algorithms Implemented

| Algorithm | Application |
|---|---|
| Merge Sort | Parcel prioritization |
| 0/1 Knapsack (Dynamic Programming) | Optimal parcel selection |
| Dijkstra's Algorithm | Shortest path calculation |
| Nearest Neighbor TSP | Delivery route planning |

## Project Structure

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
├── docs/
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

## Installation and Execution

### 1. Clone or download the project

Open the project folder in Visual Studio Code.

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run the application

```powershell
python main.py
```

## Application Menu

The application provides four options:

1. View All Parcels
2. Generate Courier Delivery Plan
3. Find Shortest Path
4. Exit

## Sample Dataset

The application uses eight sample parcels with the following attributes:

- Parcel ID
- Destination
- Weight
- Priority
- Deadline
- Delivery Value

The vehicle capacity is set to 20 kg.

The road network consists of seven locations: Warehouse, A, B, C, D, E and F.

## Sample Results

The application selects four parcels:

- P04
- P06
- P01
- P07

Total selected weight: 20 kg

Maximum delivery value: ₹2,050

Final delivery route:

Warehouse → A → D → F → Warehouse

Total route distance: 36 km

## Performance Testing

The project measures the execution time of all four algorithms.

Parcel dataset sizes:
- 8
- 50
- 100
- 200

Graph sizes:
- 10
- 25
- 50
- 100 vertices

The results are saved as CSV files and visualized using Matplotlib charts.

Run performance testing using:

```powershell
python performance.py
```

## Time Complexity

| Algorithm | Time Complexity |
|---|---|
| Merge Sort | O(n log n) |
| 0/1 Knapsack | O(nW) |
| Dijkstra | O((V + E) log V) |
| Nearest Neighbor TSP | O(k²) after shortest-path distances are available |

## Limitations

- The road network uses simulated distances.
- The vehicle capacity is fixed at 20 kg.
- The parcel dataset is predefined.
- Nearest Neighbor is an approximation and does not guarantee the globally shortest TSP route.
- Performance measurements depend on the computer and execution environment.

## Future Enhancements

- Add real-time road distances and traffic information.
- Support multiple delivery vehicles.
- Allow users to add parcels dynamically.
- Introduce a graphical user interface.
- Implement more advanced route optimization techniques.

## Conclusion

The Mini-Courier-Planner demonstrates how sorting, dynamic programming, shortest-path algorithms and approximation techniques can be integrated into a single application to solve a practical courier planning problem.

The project provides parcel prioritization, optimized package selection, shortest-path calculation, delivery route planning and algorithm performance analysis.