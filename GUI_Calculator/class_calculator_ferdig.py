'''
Calculator Class

This program implements a `Calculator` class to perform basic arithmetic operations and maintain a log of calculations. It demonstrates object-oriented programming concepts, including encapsulation and state management.

## Class: Calculator
Represents a simple arithmetic calculator.

### Attributes:
- `log`: A list that stores a history of calculations performed.

### Methods:
1. **`calculate(operand1, operand2, operator)`**:
   - Performs an arithmetic operation (`+`, `-`, `*`, `/`) on two operands.
   - Appends the calculation and result as a formatted string to the `log`.
   - Returns the result of the calculation.
   - Returns `None` if an invalid operator is provided.

2. **`get_log()`**:
   - Returns the full log of calculations as a list of strings.

3. **`get_last_logged()`**:
   - Returns the last calculation performed as a string.

4. **`clear_log()`**:
   - Clears the calculation log.

## main() function provided for simple functionality testing

## Applications
- Basic arithmetic operations in educational tools.
- Demonstrates log management in small-scale computational systems.
- Provides a framework for extending functionality to support advanced operations or a graphical user interface (GUI).
'''
class Calculator:
    def __init__(self):
        self.log = []

    def calculate(self,operand1,operand2,operator):
        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2 
        elif operator == "/":
            result = operand1 / operand2
        else:
            result = None

        if result is not None:
            log_line = f"{operand1} {operator} {operand2} = {result}"
            self.log.append(log_line)
            return result
        else:
            return None 

    def get_log(self):
        return self.log

    def get_last_logged(self):
        return self.log[-1]

    def clear_log(self):
        self.log = []

#def main():
#    calculator = Calculator()
#    calculator.calculate(1,2,'+')
#    calculator.calculate(2,2,'*')
#    calculator.calculate(16,2,'/')
#    print(calculator.get_log())
#    print(calculator.get_last_logged())

#main()


