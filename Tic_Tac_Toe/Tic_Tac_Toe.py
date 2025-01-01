'''
Tic-Tac-Toe Game

This program implements a two-player Tic-Tac-Toe game in Python.

- **Features**:
  1. The game board is displayed in a grid format.
  2. Players take turns to input their move by specifying a row and column position.
  3. The program validates moves to ensure players can only place their mark in empty positions.
  4. Checks for win conditions (horizontal, vertical, and diagonal) after each move.
  5. Detects if the game ends in a tie when the board is full.

- **Functions**:
  1. `printboard()`: Displays the current state of the game board.
  2. `winner(player)`: Checks if the specified player has won.
  3. `tie()`: Checks if the game is a tie (all positions filled without a winner).
  4. `main()`: Contains the main game loop where players take turns and game logic is executed.

- **How to Play**:
  - Players "X" and "O" alternate turns.
  - Enter row and column positions (0, 1, or 2) to place your mark.
  - The game announces the winner or a tie when the game ends.

This program demonstrates core programming concepts like nested loops, conditionals, and function organization.
'''

#Create a board
board = [[" " for _ in range (3)] for _ in range (3)]

#funktion printing the board

def printboard ():
    print ("-------------")
    for row in board:
        print ("|", end=" ")
        for cell in row:
            print (cell, end=" | ")
        print ("\n-------------")


#function to check if a player won

def winner (player):
    for row in board:
        if all(cell == player for cell in row):
            return True
        else:
            return False
        
    for column in row:
        if all(board [row][column] == player for row in range (3)):
            return True
        else:
            return False
        
    if all(board [_][_] == player for _ in range (3)) or all(board [_][2 - _] == player for _ in range (3)):
        return True
    else:
        return False


#funktion to check if its a tie

def tie():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

#game loop

def main():
    player = "X"

    while True: 
        printboard ()
        row = int(input(f"Enter a row possition for player {player} (0,1 or 2)"))
        column = int(input(f"Enter a column possition for player {player} (0,1 or 2)"))

        if board [row][column] == " ":
            board [row][column] = player
        else:
            print ("This possition is taken. Try again")
            continue

        if winner (player) == True:
            printboard ()
            print (f"{player} won")
            break

        if tie () == True:
            print ("It's a tie")
            break

        player = "0" if player == "X" else "X"



main()
