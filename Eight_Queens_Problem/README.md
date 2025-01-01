# Eight Queens Problem

This folder contains a Python implementation of the Eight Queens problem. 
The goal is to place eight queens on an 8x8 chessboard such that no two queens threaten each other.

---

## Features
- **Chessboard Representation**: The board is represented as a list of column positions for queens in each row.
- **Validation**: Checks if the current board configuration satisfies the rules:
  - No two queens share the same row, column, or diagonal.
- **Visualization**: Displays the chessboard with queens marked as "X".

---

## How It Works
1. **Class `EQ`**:
   - Stores the chessboard state.
   - Provides methods to set queen positions, validate the board, and display it.
2. **Main Function**:
   - Demonstrates the functionality by manually placing queens on the board.
   - Checks if the placement is a valid solution.
   - Prints the chessboard for visualization.

---

## How to Run
Run the program in a Python environment:
```bash
python3 Eight_Queens_Problem.py
