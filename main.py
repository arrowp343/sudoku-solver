import sys
from Sudoku import *

def get_param():

    #return "....6.9...2...8.3...53....7...5....9..1.7....3....25..5....3.4...7.1.6...8.4....."

    if len(sys.argv) != 2:
        print("Missing Argument!")
        sys.exit(1)

    param = sys.argv[1]

    if len(param) != 9**2:
        print(f"Error: The input must be exactly 81 characters long. (actual length: {str(len(param))} )")
        sys.exit(1)

    print(f"Received parameter: {param}")
    return param

def main():
    input_string = get_param()
    sudoku = Sudoku(input_string)
    sudoku.print()

if __name__ == "__main__":
    main()

