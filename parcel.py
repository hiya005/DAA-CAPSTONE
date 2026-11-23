from dataclasses import dataclass

@dataclass
class Parcel:
    parcel_id: str
    destination: str
    weight: int
    priority: int
    deadline: int 
    value: int

# Sample parcel dataset 
parcels = [
    Parcel("P01", "A", 5, 4, 2, 500),
    Parcel("P02", "B", 8, 5, 1, 800),
    Parcel("P03", "C", 4, 3, 3, 400),
    Parcel("P04", "D", 7, 5, 2, 700),
    Parcel("P05", "E", 3, 2, 4, 300),
    Parcel("P06", "F", 6, 4, 1, 600),
    Parcel("P07", "A", 2, 3, 2, 250),
    Parcel("P08", "C", 9, 1, 5, 350),
]