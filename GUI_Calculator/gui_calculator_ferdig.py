'''
Graphical User Interface (GUI) Calculator

This program implements a GUI for a basic calculator using the `tkinter` library. It leverages the `Calculator` class (from `class_calculator_ferdig`) to perform arithmetic operations and maintain a log of calculations.

## Class: Calculator_GUI
Represents the graphical user interface for the calculator.

### Features:
1. **User Inputs**:
   - Accepts two operands and an operator (`+`, `-`, `*`, `/`) via text entry fields.

2. **Result Display**:
   - Shows the result of the calculation in a dedicated label.

3. **Log Management**:
   - Displays a log of all calculations performed.
   - Allows clearing the log via a button.

4. **Interactive Buttons**:
   - **Calculate**: Performs the calculation based on user inputs.
   - **Clear Log**: Clears the log of calculations.
   - **Quit**: Closes the GUI.

### Methods:
1. **`__init__()`**:
   - Initializes the GUI layout and its components.
   - Creates instances of the `Calculator` class to handle calculations.
   - Sets up input fields, buttons, and labels.

2. **`calculate()`**:
   - Retrieves user inputs for operands and operator.
   - Uses the `Calculator` class to perform the calculation.
   - Updates the result display and log.

3. **`show_log()`**:
   - Retrieves and displays the calculation log in the GUI.

4. **`clear_log()`**:
   - Clears the calculation log and updates the GUI display.

### Usage
Run the program, and the GUI will open. Enter values for operands and an operator, then click "Calculate" to perform a calculation. View the result and calculation history directly in the interface.

### Example
1. **Input**:
   - Operand 1: `5`
   - Operand 2: `3`
   - Operator: `+`

2. **Output**:
   - Result: `8.0`
   - Log:
     ```
     5.0 + 3.0 = 8.0
     ```

3. **Clear Log**: Removes all entries from the log display.

## Applications
- Educational tools for basic arithmetic.
- Demonstrates integration of a functional backend with a graphical user interface.
- Foundation for building more complex calculators or computational tools.
'''

from tkinter import *
from class_calculator_ferdig import Calculator

class Calculator_GUI:
    def __init__(self):
        self.calculator = Calculator()

        window = Tk()
        window.title("GUI Calculator")
        Label(window, text = "Operand 1: ").grid(row = 1, column = 1)
        Label(window, text = "Operator (+ - / *): ").grid(row = 2, column = 1)
        Label(window, text = "Operand 2: ").grid(row = 3, column = 1)
        Label(window, text = "Result: ").grid(row = 5, column = 1)
        Label(window, text = "Log: ").grid(row = 6, column = 1)
        
        Button(window, text = "Calculate", command = self.calculate).grid(row = 4, column = 1)
        Button(window, text = "Clear log", command = self.clear_log).grid(row = 4, column = 2)
        Button(window, text = "Quit", command = window.quit).grid(row = 4, column = 3)
        
        self.operand1 = StringVar()
        Entry(window, textvariable = self.operand1).grid(row = 1, column = 2, padx = 5, pady = 5)
        
        self.operator = StringVar()
        Entry(window, textvariable = self.operator).grid(row = 2, column = 2, padx = 5, pady = 5)

        self.operand2 = StringVar()
        Entry(window, textvariable = self.operand2).grid(row = 3, column = 2, padx = 5, pady = 5)

        self.result = StringVar()
        Label(window, textvariable = self.result).grid(row = 5, column = 2)

        self.log_display = Text(window, height = 5, width = 30)
        self.log_display.grid(row = 7, column =1, columnspan = 2)
        
        window.mainloop()

    def calculate(self):
        operand1 = float(self.operand1.get())
        operand2 = float(self.operand2.get())
        operator = self.operator.get()
        result = self.calculator.calculate(operand1, operand2, operator)
        self.result.set(result)
        self.show_log()

        
    def show_log(self):
        log = self.calculator.get_log()
        self.log_display.delete(1.0, END)
        for entry in log:
            self.log_display.insert(END, entry + "\n")


    def clear_log(self):
        self.calculator.clear_log()
        self.show_log()
    
Calculator_GUI()



        