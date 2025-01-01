'''
Eight Queens Problem

This program implements a solution for the Eight Queens problem, where the objective is to place eight queens on an 8x8 chessboard such that no two queens threaten each other. The program provides functionality to set queen positions, validate the board, and display the chessboard.

## Class: EQ
Represents the chessboard and queen placements.

### Attributes:
- `queens`: A list of integers representing the column positions of queens in each row. Default is `[-1, -1, ..., -1]` (empty board).

### Methods:
1. `get(i)`: Returns the column position of the queen in row `i`.
2. `set(i, j)`: Places a queen in row `i` and column `j`.
3. `isSolved()`: Validates the board to check if the current queen placements satisfy the rules of the Eight Queens problem:
   - No two queens share the same row, column, or diagonal.
4. `printBoard()`: Prints the 8x8 chessboard with queens marked as "X".

## Main Function:
- Creates an instance of the EQ class.
- Sets queen positions manually.
- Checks if the board is a valid solution.
- Prints the board configuration.
'''

class EQ ():

    def __init__(self, queens=8 * [-1]):
        self.queens = queens
       
       
     #get the possition of the queen in a row  
    def get (self,i):
        return self.queens[i]
    
    #set the possition of a queen
    def set (self,i,j):
        self.queens [i] = j

    #check placement of queens
    def isSolved (self):
        for i in range (8):
            for j in range (i + 1, 8):
                if self.queens [i] == self.queens [j] or abs(self.queens[i]-self.queens[j]) == abs(i-j):
                    return False 
                else: return True
    
    def printBoard(self):
        for i in range (8):
            row = " |" 
            for j in range (8):
                if self.queens [i] == j:
                    row += "X|"
                else: 
                    row += " |"
            print (row)
        

def main():
    board1 = EQ()

    board1.set(0, 2)

    board1.set(1, 4)

    board1.set(2, 7)

    board1.set(3, 1)

    board1.set(4, 0)

    board1.set(5, 3)

    board1.set(6, 6)

    board1.set(7, 5)

    print("Is board1 a correct eight queen placement?",

        board1.isSolved())
    
    board1.printBoard ()
    
main()


    
        

        


