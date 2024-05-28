import sys
from Sudoku import *
from Sudoku_Solver import *
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Argument Error! Arguments required: <N (size of sudoku)> <sudoku string (with length N**2)>")
        sys.exit(1)

    N = int(sys.argv[1])
    sudoku_string = sys.argv[2]

    #sudoku_string = "....6.9...2...8.3...53....7...5....9..1.7....3....25..5....3.4...7.1.6...8.4....."
    #N = 9

    sudoku = Sudoku(N, sudoku_string)

    s_solver = Sudoku_Solver()
    s_solver.solve(sudoku)

    sys.exit(0)