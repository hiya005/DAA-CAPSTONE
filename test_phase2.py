
from parcel import parcels
from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack


# Step 1: Sort parcels
sorted_parcels = merge_sort(parcels)

print("===== SORTED PARCELS =====")

for p in sorted_parcels:
    print(
        p.parcel_id,
        p.destination,
        p.weight,
        p.priority,
        p.deadline,
        p.value
    )


# Step 2: Apply Knapsack
capacity = 20

selected, total_value, dp = knapsack(
    sorted_parcels, capacity
)

print("\n===== SELECTED PARCELS =====")

total_weight = 0

for p in selected:
    print(p.parcel_id, "-", p.destination,
          "-", p.weight, "kg")

    total_weight += p.weight


print("\nTotal Weight:", total_weight, "kg")
print("Vehicle Capacity:", capacity, "kg")
print("Maximum Delivery Value: Rs.", total_value)


# Step 3: Display DP table
print("\n===== DP TABLE =====")

for row in dp:
    print(row)
