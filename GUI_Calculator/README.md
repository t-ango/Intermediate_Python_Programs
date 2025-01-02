# GUI Calculator with Calculation Log

This folder contains a GUI-based calculator implemented using the `tkinter` library in Python. 
The program integrates a `Calculator` backend class for performing arithmetic operations and maintaining a log of calculations.

---

## Features

1. **Calculator Class (`class_calculator_ferdig.py`)**:
   - Performs arithmetic operations: addition, subtraction, multiplication, and division.
   - Maintains a log of calculations with inputs and results.
   - Provides methods to retrieve or clear the calculation log.

2. **GUI Calculator (`gui_calculator.py`)**:
   - Graphical interface for user interaction.
   - Accepts two operands and an operator as inputs.
   - Displays the result of the calculation.
   - Shows a log of all calculations performed.
   - Includes buttons to calculate, clear the log, or quit the application.

---

## How to Run
1. Clone the repository and navigate to the folder containing the files.
2. Run the GUI Calculator:
   ```bash
   python3 gui_calculator.py
The GUI will open. Enter values for operands and an operator, then click "Calculate" to perform calculations.
Example Usage

Input:
Operand 1: 6
Operator: /
Operand 2: 2
Output:
Result: 3.0
Log:
6.0 / 2.0 = 3.0

**Applications**

Demonstrates integration of OOP concepts with a graphical user interface.
Serves as a foundation for more advanced GUI-based tools or calculators.
Useful as an educational tool for understanding basic arithmetic and GUI programming.

**Requirements**

Python 3.x
tkinter (comes pre-installed with Python on most systems)
