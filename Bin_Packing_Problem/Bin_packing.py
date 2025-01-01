'''
Bin Packing Problem

This program solves the bin-packing problem, which involves packing objects of varying weights into bins with a fixed weight capacity, minimizing the number of bins used.

## Classes

### 1. `Bin`
Represents a single bin with the following attributes and methods:
- **Attributes**:
  - `maxWeight`: The maximum weight capacity of the bin (default: 10).
  - `totalWeight`: The current total weight of objects in the bin.
  - `objects`: A list of weights of objects in the bin.
- **Methods**:
  - `addItem(weight)`: Adds an object to the bin if it fits within the remaining weight capacity. Returns `True` if successful, `False` otherwise.
  - `getNumberOfObjects()`: Returns the number of objects in the bin.
  - `__str__()`: Returns a space-separated string of object weights in the bin.

## Functions

### 2. `pack_objects(object_weights)`
- Implements a greedy algorithm to pack objects into bins.
- Iterates over the list of object weights:
  - Tries to add the current object to an existing bin.
  - If no bin can accommodate the object, creates a new bin for it.
- Returns a list of `Bin` objects.

## Main Function
- Prompts the user to input weights of objects (separated by spaces).
- Uses the `pack_objects` function to distribute the objects into bins.
- Outputs:
  - Total number of bins used.
  - The weights of objects in each bin.
'''

class Bin:
    def __init__(self, maxWeight=10):
        self.maxWeight = maxWeight
        self.totalWeight = 0
        self.objects = []

    def addItem(self, weight):
        if self.totalWeight + weight <= self.maxWeight:
            self.objects.append(weight)
            self.totalWeight += weight
            return True
        else:
            return False

    def getNumberOfObjects(self):
        return len(self.objects)

    def __str__(self):
        return " ".join(map(str, self.objects))


def pack_objects(object_weights):
    bins = []
    for weight in object_weights:
        packed = False
        for bin in bins:
            if bin.addItem(weight):
                packed = True
                break
        if not packed:
            new_bin = Bin()
            new_bin.addItem(weight)
            bins.append(new_bin)

    return bins


def main():
    object_weights = [int(w) for w in input("Enter the weights of objects (separated by spaces): ").split()]
    bins = pack_objects(object_weights)

    print("\nNumber of bins needed:", len(bins))

    for i, bin in enumerate(bins):
        print(f"Bin {i + 1}: {bin}")

if __name__ == "__main__":
    main()
