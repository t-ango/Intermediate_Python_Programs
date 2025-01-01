# Bin Packing Problem

This folder contains a Python implementation of the bin-packing problem, 
which optimizes the packing of objects with varying weights into bins with a fixed weight capacity.

---

## Features
1. **Bin Class**:
   - Represents a bin with a maximum weight capacity.
   - Tracks the current total weight and objects in the bin.
   - Allows adding objects if they fit within the bin's remaining capacity.

2. **Greedy Algorithm**:
   - Packs objects into bins using a first-fit strategy.
   - Minimizes the number of bins required.

3. **User Interaction**:
   - Prompts the user to input object weights.
   - Outputs the total number of bins used and their contents.

---

## How to Run
1. Run the program:
   ```bash
   python3 bin_packing.py
   
2. Enter the weights of the objects when prompted, separated by spaces:
   Enter the weights of objects (separated by spaces): 2 5 4 7 1 3 8
   
4. View the output:
Number of bins needed: 4
Bin 1: 2 5
Bin 2: 4 3
Bin 3: 7
Bin 4: 8

**Applications**

Logistics and Transportation:
Optimizing the packing of goods into containers or vehicles.
Inventory Management:
Grouping items into storage units efficiently.
Algorithm Design:
Demonstrates the use of greedy algorithms for optimization problems.

**Requirements**

Python 3.x
