# Tic-Tac-Toe

A Python implementation of the classic two-player game, Tic-Tac-Toe.

## About
Tic-Tac-Toe is a simple yet engaging game played on a 3x3 grid. Players alternate turns, marking spaces on the grid with their respective symbols ("X" or "O"). 
The objective is to align three symbols in a row, column, or diagonal. This implementation allows two players to play alternately in a text-based interface.

---

## Features
- **Two-Player Mode**: Players "X" and "O" take turns.
- **Win Detection**: The program detects and announces when a player wins (row, column, or diagonal alignment).
- **Tie Detection**: Declares a tie when all grid spaces are filled without a winner.
- **Input Validation**: Ensures players can only place symbols in empty spaces.

---

## How to Play
1. Run the program:
   ```bash
   python3 tic_tac_toe.py
The program will display a 3x3 grid representing the game board:
-------------
|   |   |   | 
-------------
|   |   |   | 
-------------
|   |   |   | 
-------------
Players take turns to input their move:
Enter the row and column numbers (0, 1, or 2) to place your mark.
The game ends when:
A player aligns three symbols in a row, column, or diagonal.
The grid is full, resulting in a tie.
Example Gameplay

Player X, enter row position (0, 1, or 2): 0
Player X, enter column position (0, 1, or 2): 1

-------------
|   | X |   | 
-------------
|   |   |   | 
-------------
|   |   |   | 
-------------

**Code Structure**
printboard(): Displays the current state of the game board.
winner(player): Checks if the specified player has won the game.
tie(): Checks if the game ends in a tie.
main(): The main game loop where players take turns and the game logic is executed.

**Requirements**
Python 3.x

**Future Enhancements**

Add an AI opponent for single-player mode.
Create a graphical interface for a more user-friendly experience.
Allow players to customize their symbols.
